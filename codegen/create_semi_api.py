""" Scipt to create a ...
"""

import os
import sys
import ctypes  # not actually used, but handy to have imported during dev

import headerparser
from annotations import parse_anotations

from OpenGL import GL  # For checking

THISDIR = os.path.abspath(os.path.dirname(__file__))
GLDIR = os.path.join(THISDIR, '..', 'vispy', 'gloo', 'gl2')

PREAMBLE = '''"""

THIS CODE IS AUTO-GENERATED. DO NOT EDIT.

%s

"""
'''

## Create parsers

# Create a parser for desktop and web gl
parser1 = headerparser.Parser(os.path.join(THISDIR, 'headers', 'gl2.h'))
headerparser.CONSTANTS = {}
parser2 = headerparser.Parser(os.path.join(THISDIR, 'headers', 'webgl.idl'))

# Get annotations
annotations = parse_anotations()


## Check constants

# Get names
names1 = set(parser1.constant_names)
names2 = set(parser2.constant_names)

# Check names correspondence
if names1 == names2:
    print('Constants in gl2 and webgl are equal')
else:
    print('===== Extra names in gl2 =====')
    print(', '.join(names1.difference(names2)))
    print('===== Extra names in webgl =====')
    print(', '.join(names2.difference(names1)))
    print('===========')

# Test value correspondence
superset = names1.intersection(names2)
#
constants = {}
for c1 in parser1.constants.values():
    if c1.pname in superset:
        constants[c1.pname] = c1.value
#
assert len(constants) == len(superset)
#
for c2 in parser2.constants.values():
    if c2.pname in constants:
        assert c2.value == constants[c2.pname]
print('Hooray! All constants that occur in both namespaces have equal values.')


def create_constants_module(parser, extension=False):

    # Initialize
    lines = []
    lines.append(PREAMBLE % 'Constants for OpenGL ES 2.0.')

    # __future__ import
    lines.append(
        'from __future__ import print_function, division, absolute_import\n')

    # Import enum
    lines.append('from . import _GL_ENUM')
    lines.append('\n')

    # For extensions, we only take the OES ones, and remove the OES
    if extension:
        constantDefs = []
        for c in parser.constants.values():
            if 'OES' in c.oname:
                c.oname = c.oname.replace('OES','')
                c.oname = c.oname.replace('__','_').strip('_')
                constantDefs.append(c)
    else:
        constantDefs = parser.constants.values()

    # Insert constants
    for c in sorted(constantDefs, key=lambda x: x.oname):
        if isinstance(c.value, int):
            lines.append('%s = _GL_ENUM(%r, %r)' % (c.oname, c.oname, c.value))
        else:
            lines.append('%s = %r' % (c.oname, c.value))
    lines.append('')

    # Write the file
    fname = '_constants_ext.py' if extension else '_constants.py'
    with open(os.path.join(GLDIR, fname), 'wb') as f:
        f.write(('\n'.join(lines)).encode('utf-8'))
    print('wrote %s' % fname)
    

create_constants_module(parser1)


## List functions

IGNORE_FUNCTIONS = ['releaseShaderCompiler', 'shaderBinary']

WEBGL_EQUIVALENTS = {   
                        'genBuffers': 'createBuffer',
                        'genFramebuffers': 'createFramebuffer',
                        'genRenderbuffers': 'createRenderbuffer',
                        'genTextures': 'createTexture',
                        
                        'deleteBuffers': 'deleteBuffer',
                        'deleteFramebuffers': 'deleteFramebuffer',
                        'deleteRenderbuffers': 'deleteRenderbuffer',
                        'deleteTextures': 'deleteTexture',
                        
                        'clearDepthf': 'clearDepth',
                        'depthRangef': 'depthRange',
                        
                        'getBufferParameteriv': 'getBufferParameter',
                        'getRenderbufferParameteriv': 'getRenderbufferParameter',
                        'getFramebufferAttachmentParameteriv': 'getFramebufferAttachmentParameter',
                        
                        'getVertexAttribPointerv': 'getVertexAttribOffset',
                        
                        'getProgramiv': 'getProgramParameter',
                        'getShaderiv': 'getShaderParameter',
                        
                        'getBooleanv': 'getParameter',
                        'getFloatv': 'getParameter',
                        'getIntegerv': 'getParameter',
                        'getString': 'getParameter',
                    }


EASY_TYPES = {  'void': (type(None), 'c_voidp'),  # only for output
                'GLenum': (int, 'c_uint'),
                'GLboolean': (bool, 'c_bool'),
                'GLuint': (int, 'c_uint'),
                'GLint': (int, 'c_int'),
                'GLbitfield': (int, 'c_uint'),
                'GLsizei': (int, 'c_int'),
                'GLfloat': (float, 'c_float'),
                'GLclampf': (float, 'c_float'),
             }

# Types that dont map 1-on-1 to Python values, but that we know
# how to set the ctypes argtypes for. Together with the EASY_TYPES
# we should cover all types that ES 2.0 uses.
HARDER_TYPES = {
                'GLenum*':('', 'POINTER(ctypes.c_uint)'),
                'GLboolean*':('', 'POINTER(ctypes.c_bool)'),
                'GLuint*':('', 'POINTER(ctypes.c_uint)'),
                'GLint*':('', 'POINTER(ctypes.c_int)'),
                'GLsizei*':('', 'POINTER(ctypes.c_int)'),
                'GLfloat*':('', 'POINTER(ctypes.c_float)'),
                
                'GLubyte*':('', 'c_char_p'),
                'GLchar*':('', 'c_char_p'),
                'GLchar**':('', 'POINTER(ctypes.c_char_p)'),
                'GLvoid*':('', 'c_void_p'),  # or c_voidp?
                'GLvoid**':('', 'POINTER(ctypes.c_void_p)'),
                'GLintptr':('', 'c_int'), 
                'GLsizeiptr':('', 'c_int'),
                }


KNOWN_TYPES = EASY_TYPES.copy()
KNOWN_TYPES.update(HARDER_TYPES)


FUNC_WITH_ARRAY = """
if not data.flags['C_CONTIGUOUS']:
    data = data.copy('C')
data_ = data
%s = data_.size
data = data_.ctypes.data
""".strip()


# Keep track of what webGL names we "used"
used_webgl_names = set()

# Also keep track of what functions we could handle automatically, 
# and which not. Just for reporting.
functions_auto = set()
functions_anno = set()
functions_todo = set()



class FunctionDescription:
    def __init__(self, name, es2func, wglfunc, annfunc):
        self.name = name
        self.es2 = es2func
        self.wgl = wglfunc
        self.ann = annfunc
        self.args = []


def combine_function_definitions():
    """ Process function definitions of ES 2.0, WebGL and annotations.
    We try to combine information from these three sources to find the
    arguments for the Python API. In this "merging" process we also
    check for inconsistencies between the API definitions.
    """
    functions = []
    
    for name in parser1.function_names:
        if name in IGNORE_FUNCTIONS:
            continue
        
        # Get es2 function
        es2func = parser1.functions[name]
        
        # Get webgl version
        lookupname = WEBGL_EQUIVALENTS.get(es2func.pname, es2func.pname)
        wglfunc = parser2.functions.get(lookupname, None)
        if wglfunc:
            used_webgl_names.add(lookupname)
        else:
            print('WARNING: %s not available in WebGL' % es2func.pname)
        
        # Convert name
        if name.startswith('gen'):
            name = 'create' + name[3:-1]
        elif name.startswith('delete'):
            name = name[:-1]
        
        # Get annotated version
        annfunc = annotations.get(name, None)
        
        # Create description instance
        des = FunctionDescription(name, es2func, wglfunc, annfunc)
        functions.append(des)
        
        # Get information about arguments
        if True:
            argnames_es2 = [arg.name for arg in es2func.args[1:]]
            argtypes_es2 = [EASY_TYPES.get(arg.ctype, None) for arg in es2func.args]
        if wglfunc:
            argnames_wgl = [arg.name for arg in wglfunc.args[1:]]
            argtypes_wgl = [EASY_TYPES.get(arg.ctype, None) for arg in wglfunc.args]
        if annfunc:
            argnames_ann = annfunc.args
        
        # Process 
        if wglfunc and argnames_es2 == argnames_wgl:
            if annfunc and argnames_ann != argnames_es2:
                des.args = argnames_ann
                print('WARNING: %s: Annotation overload even though webgl and es2 match.'%name)
            else:
                des.args = argnames_es2
        elif wglfunc:
            if annfunc and argnames_ann != argnames_wgl:
                des.args = argnames_ann
                print('WARNING: %s: Annotation overload webgl args.'%name)
            else:
                #print('WARNING: %s: assuming wgl args.'%name)
                des.args = argnames_wgl
        else:
            print('WARNING: %s: Could not determine args!!'%name)
        
        
        # Go over all functions to test if they are in OpenGL
        for func in [es2func, wglfunc]:
            if func is None: 
                continue
            group = func.group or [func]
            for f in group:
                # Check opengl
                if f.oname.startswith('gl') and not hasattr(GL, f.glname):
                    print('WARNING: %s seems not available in PyOpenGL' % f.pname)
    
    return functions



class ApiGenerator:
    PREAMBLE = ""
    def __init__(self):
        self.lines = []
    
    def save(self):
        with open(self.filename, 'wb') as f:
            f.write((PREAMBLE % 'GL API X').encode('utf-8'))
            for line in self.PREAMBLE.splitlines():
                f.write(line[4:].encode('utf-8')+b'\n')
            for line in self.lines:
                f.write(line.encode('utf-8')+b'\n')
    
    def add_function(self, des):
        if des.es2.group:
            self._add_function_group(des)
        else:
            self._add_function(des)
        self.lines.append('\n')  # two lines between each function
    
    
    def _add_function_group(self, des):
        lines = self.lines
        handled = True
        
        # Create map to es2 function objects
        es2funcs = {}
        for f in des.es2.group:
            cname = f.oname[2].lower() + f.oname[3:]
            es2funcs[cname] = f
        
        if des.name == 'uniform':
            for t in ('float', 'int'):
                for i in (1,2,3,4):
                    args = ', '.join(['v%i'%j for j in range(1,i+1)])
                    cname = 'uniform%i%s' % (i, t[0])
                    sig = '%s(location, %s)' % (cname, args)
                    self._add_group_function(des, sig, es2funcs[cname])
            for t in ('float', 'int'):
                for i in (1,2,3,4):
                    cname = 'uniform%i%sv' % (i, t[0])
                    sig = '%s(location, count, values)' % cname
                    self._add_group_function(des, sig, es2funcs[cname])
        elif des.name == 'uniformMatrix':
            for i in (2,3,4):
                cname = 'uniformMatrix%ifv' % i
                sig = '%s(location, count, transpose, values)' % cname
                self._add_group_function(des, sig, es2funcs[cname])
        elif des.name == 'getUniform':
            for t in ('float', 'int'):
                cname = 'getUniform%sv' % t[0]
                sig = '%s(program, location)' % cname
                self._add_group_function(des, sig, es2funcs[cname])
        
        elif des.name == 'vertexAttrib':
            for i in (1,2,3,4):
                args = ', '.join(['v%i'%j for j in range(1,i+1)])
                cname = 'vertexAttrib%if' % i
                sig = '%s(index, %s)' % (cname, args)
                self._add_group_function(des, sig, es2funcs[cname])
        elif des.name == 'getVertexAttrib':
            for t in ('float', 'int'):
                cname = 'getVertexAttrib%sv' % t[0]
                sig = '%s(index, pname)' % cname
                self._add_group_function(des, sig, es2funcs[cname])
        
        elif des.name == 'texParameter':
            for t in ('float', 'int'):
                cname = 'texParameter%s' % t[0]
                sig = '%s(target, pname, param)' % cname
                self._add_group_function(des, sig, es2funcs[cname])
        elif des.name == 'getTexParameter':
            for t in ('float', 'int'):
                cname = 'getTexParameter%sv' % t[0]
                sig = '%s(target, pname)' % cname
                self._add_group_function(des, sig, es2funcs[cname])
        
        else:
            handled = False
        
        if handled:
            functions_auto.add(des.name)
        else:
            functions_todo.add(des.name)
            lines.append('# todo: Dont know group %s' % des.name)
    
    def _add_function(self, des):
        raise NotImplementedError()
    
    def _add_group_function(self, des, sig, es2func):
        raise NotImplementedError()



class MainApiGenerator(ApiGenerator):
    #filename = os.path.join(THISDIR, 'api_main.py')
    filename = os.path.join(GLDIR, '_main.py')
    
    def _add_function(self, des):
        argstr = ', '.join(des.args)
        self.lines.append('def %s(%s):' % (des.name, argstr))
        self.lines.append('    return PROXY["%s"](%s)' % (des.name, argstr))
    
    def _add_group_function(self, des, sig, es2func):
        funcname = sig.split('(')[0]
        args = sig.split('(', 1)[1].split(')')[0]
        self.lines.append('def %s:' % sig)
        self.lines.append('    return PROXY["%s"](%s)' % (funcname, args))



class CompatApiGenrator(MainApiGenerator):
    filename = os.path.join(GLDIR, '_main_compat.py')
    write_c_sig = False
    
    PREAMBLE = """
    from .import _main
    PROXY = _main.__dict__
    """
    def _add_function(self, des):
        argstr = ', '.join(des.args)
        name = 'gl' + des.name[0].upper() + des.name[1:]
        self.lines.append('def %s(%s):' % (name, argstr))
        self.lines.append('    return PROXY["%s"](%s)' % (des.name, argstr))
    
    def _add_group_function(self, des, sig, es2func):
        funcname = sig.split('(')[0]
        sig = 'gl' + sig[0].upper() + sig[1:]
        args = sig.split('(', 1)[1].split(')')[0]
        self.lines.append('def %s:' % sig)
        self.lines.append('    return PROXY["%s"](%s)' % (funcname, args))



class DesktopApiGenerator(ApiGenerator):
    filename = os.path.join(GLDIR, '_desktop.py')
    write_c_sig = True
    
    PREAMBLE = """
    import ctypes.util
    import sys
    
    if sys.platform.startswith('win'):
        fname = ctypes.util.find_library('opengl32')
        #_lib = ctypes.cdll.LoadLibrary(fname)  # Actually works as well
        _lib = ctypes.windll.opengl32#(fname, ctypes.RTLD_GLOBAL)
        
        try:
            wglGetProcAddress = _lib.wglGetProcAddress
            wglGetProcAddress.restype = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))
            wglGetProcAddress.argtypes = [ctypes.c_char_p]
            _have_get_proc_address = True
        except AttributeError:
            _have_get_proc_address = False
    else:
        _have_get_proc_address = False
        fname = ctypes.util.find_library('GL')
        _lib = ctypes.cdll.LoadLibrary(fname)
    
    del sys
    
    def _have_context():
        return _lib.glGetError() != 1282  # GL_INVALID_OPERATION


    def _get_gl_func(name, restype, argtypes):
        try:
            # Try using normal ctypes stuff
            func = getattr(_lib, name)
            func.restype = restype
            func.argtypes = argtypes
            return func
        except AttributeError:
            # Ask for a pointer to the function, this is the approach
            # for OpenGL extensions on Windows 
            fargs = (restype,) + argtypes
            ftype = ctypes.WINFUNCTYPE(*fargs)
            if not _have_get_proc_address:
                raise RuntimeError('Function %s not available.' % name)
            if not _have_context():
                raise RuntimeError('Using %s with no OpenGL context.' % name)
            address = wglGetProcAddress(name.encode('utf-8'))
            if address:
                return ctypes.cast(address, ftype)
            else:
                raise RuntimeError('Function %s not present in current context.' % name)
    """
    
    def _get_argtype_str(self, es2func):
        ce_arg_types = [arg.ctype for arg in es2func.args[1:]]
        ct_arg_types = [KNOWN_TYPES.get(arg.ctype, None) for arg in es2func.args]
        # Set argument types on ctypes function
        if None in ct_arg_types:
            argstr = 'UNKNOWN_ARGTYPES'
        elif es2func.group:
            argstr = 'UNKNOWN_ARGTYPES'
        else:
            argstr = ', '.join(['ctypes.%s' % t[1] for t in ct_arg_types[1:]])
            argstr = '()' if not argstr else '(%s,)' % argstr
        # Set output arg (if available)
        if ct_arg_types[0][0] != type(None):
            resstr = 'ctypes.%s' % ct_arg_types[0][1]
        else:
            resstr = 'None'
        return resstr, argstr
    
    
    def _write_argtypes(self, es2func):
        lines = self.lines
        ce_arg_types = [arg.ctype for arg in es2func.args[1:]]
        ct_arg_types = [KNOWN_TYPES.get(arg.ctype, None) for arg in es2func.args]
        # Set argument types on ctypes function
        if None in ct_arg_types:
            lines.append('# todo: unknown argtypes')
        elif es2func.group:
            lines.append('# todo: oops, dont set argtypes for group!')
        else:
            if ct_arg_types[1:]:
                argstr = ', '.join(['ctypes.%s' % t[1] for t in ct_arg_types[1:]])
                lines.append('_lib.%s.argtypes = %s,' % (es2func.glname, argstr))
            else:
                lines.append('_lib.%s.argtypes = ()' % es2func.glname)
        # Set output arg (if available)
        if ct_arg_types[0][0] != type(None):
            lines.append('_lib.%s.restype = ctypes.%s' % (es2func.glname, ct_arg_types[0][1]))
    
    def _native_call_line(self, name, es2func, cargstr=None, prefix='', indent=4):
        #'_lib.%s(%s)' % (des.es2.glname, cargstr)
        resstr, argstr = self._get_argtype_str(es2func)
        if cargstr is None:
            cargs = [arg.name for arg in es2func.args[1:]]
            cargstr = ', '.join(cargs)
        
        lines = 'try:\n'
        lines += '    func = %s._native\n' % name
        lines += 'except AttributeError:\n'
        lines += '    func = %s._native = _get_gl_func("%s", %s, %s)\n' % (
                name, es2func.glname, resstr, argstr)
        lines += '%sfunc(%s)' % (prefix, cargstr)
        
        lines = [' '*indent + line for line in lines.splitlines()]
        return '\n'.join(lines)
    
    def _add_function(self, des):
        lines = self.lines
        es2func = des.es2
        
        # Write arg types
        #self._write_argtypes(des.es2)
        
        # Get names and types of C-API
        ce_arg_types = [arg.ctype for arg in es2func.args[1:]]
        ce_arg_names = [arg.name for arg in es2func.args[1:]]
        ct_arg_types = [KNOWN_TYPES.get(arg.ctype, None) for arg in es2func.args]
        ct_arg_types_easy = [EASY_TYPES.get(arg.ctype, None) for arg in es2func.args]
        
        # Write C function signature, for debugging and development
        if self.write_c_sig:
            argnamesstr = ', '.join([c_type+' '+c_name for c_type, c_name in zip(ce_arg_types, ce_arg_names)])
            lines.append('# %s = %s(%s)' % (es2func.args[0].ctype, es2func.oname, argnamesstr))
        
        # Write Python function def
        lines.append('def %s(%s):' % (des.name,  ', '.join(des.args)))
        
        # Construct C function call
        cargs = [arg.name for arg in des.es2.args[1:]]
        cargstr = ', '.join(cargs)
        #callline = '_lib.%s(%s)' % (des.es2.glname, cargstr)
        
        # Now write the body of the function ...
        if des.ann:
            prefix = 'res = '
            # Annotation available
            functions_anno.add(des.name)
            callline = self._native_call_line(des.name, des.es2, prefix=prefix)
            lines.extend( des.ann.get_lines(callline, 'desktop') )
        
        elif es2func.group:
            # Group?
            functions_todo.add(des.name)
            lines.append('    pass  # todo: Oops. this is a group!')
        elif None in ct_arg_types_easy:
            functions_todo.add(des.name)
            lines.append('    pass  # todo: Not all easy types!')
        elif des.args != [arg.name for arg in des.wgl.args[1:]]:
            functions_todo.add(des.name)
            lines.append('    pass  # todo: ES 2.0 and WebGL args do not match!')
        else:
            # This one is easy!
            functions_auto.add(des.name)
            # Get prefix
            prefix = ''
            if ct_arg_types[0][0] != type(None):
                prefix = 'return '
            elif des.es2.pname.startswith('get'):
                raise RuntimeError('Get func returns void?')
            # Set string
            callline = self._native_call_line(des.name, des.es2, prefix=prefix)
            lines.append(callline)
    
    def _add_group_function(self, des, sig, es2func):
        lines = self.lines
        handled = True
        
        call_line = self._native_call_line
        
        #self._write_argtypes(es2func)
        
        funcname = sig.split('(', 1)[0]
        args = sig.split('(', 1)[1].split(')')[0]
        cfuncname = 'gl' + funcname[0].upper() + funcname[1:]
        
        if des.name == 'uniform':
            if funcname[-1] != 'v':
                lines.append('def %s:' % sig)
                lines.append(call_line(funcname, es2func, args))
            else:
                t = {'f':'float', 'i':'int'}[funcname[-2]]
                lines.append('def %s:' % sig)
                lines.append('    values = [val for val in values]')
                lines.append('    values = (ctypes.c_%s*len(values))(*values)' % t)
                lines.append(call_line(funcname, es2func, 'location, count, values'))
        elif des.name == 'uniformMatrix':
            lines.append('def %s:' % sig)
            lines.append('    values = [val for val in values]')
            lines.append('    values = (ctypes.c_float*len(values))(*values)')
            lines.append(call_line(funcname, es2func, 'location, count, transpose, values'))
        elif des.name == 'getUniform':
            t = {'f':'float', 'i':'int'}[funcname[-2]]
            lines.append('def %s:' % sig)
            lines.append('    d = -99999  # Note: this is a bit dangerous')
            lines.append('    values = (ctypes.c_%s*16)(*[d for i in range(16)])' % t)
            lines.append(call_line(funcname, es2func, 'program, location, values'))
            lines.append('    return tuple([val for val in values if val!=d])')
        
        elif des.name == 'vertexAttrib':
            lines.append('def %s:' % sig)
            lines.append(call_line(funcname, es2func, args))
        elif des.name == 'getVertexAttrib':
            t = {'f':'float', 'i':'int'}[funcname[-2]]
            lines.append('def %s:' % sig)
            lines.append('    d = -99999  # Note: this is a bit dangerous')
            lines.append('    values = (ctypes.c_%s*4)(*[d for i in range(4)])' % t)
            lines.append(call_line(funcname, es2func, 'index, pname, values'))
            lines.append('    return tuple([val for val in values if val!=d])')
        
        elif des.name == 'texParameter':
            lines.append('def %s:' % sig)
            lines.append(call_line(funcname, es2func, args))
        elif des.name == 'getTexParameter':
            t = {'f':'float', 'i':'int'}[funcname[-2]]
            lines.append('def %s:' % sig)
            lines.append('    params = (ctypes.c_%s*1)()' % t)
            lines.append(call_line(funcname, es2func, 'target, pname, params'))
            lines.append('    return params[0]')
        
        else:
            raise ValueError('unknown group func')
    
    
#     def _add_function_group_old(self, des):
#         lines = self.lines
#         handled = True
#         
#         if des.name == 'uniform':
#             for t in ('float', 'int'):
#                 for i in (1,2,3,4):
#                     args = ', '.join(['v%i'%j for j in range(1,i+1)])
#                     sig = '%i%s(location, %s)' % (i, t[0], args)
#                     lines.append('def uniform%s:' % sig)
#                     lines.append('    _lib.glUniform%s' % sig)
#             for t in ('float', 'int'):
#                 for i in (1,2,3,4):
#                     lines.append('def uniform%i%sv(location, value):' % (i, t[0]))
#                     lines.append('    values = [val for val in values]')
#                     lines.append('    values = (ctypes.c_%s*len(values))(*values)' % t)
#                     lines.append('    _lib.glUniform%i%sv(location, values)' % (i, t[0]))
#         elif des.name == 'uniformMatrix':
#             for i in (2,3,4):
#                 lines.append('def uniformMatrix%ifv(location, count, transpose, values):' % i)
#                 lines.append('    values = [val for val in values]')
#                 lines.append('    values = (ctypes.c_float*len(values))(*values)')
#                 lines.append('    _lib.glUniformMatrix%ifv(location, count, transpose, values)' % i)
#         elif des.name == 'getUniform':
#             for t in ('float', 'int'):
#                 lines.append('def getUniform%sv(program, location):' % t[0])
#                 lines.append('    d = -99999  # Note: this is a bit dangerous')
#                 lines.append('    values = (ctypes.c_%s*16)(*[d for i in range(16)])' % t)
#                 lines.append('    _lib.glGetUniform%sv(program, location, values)' % t[0])
#                 lines.append('    return tuple([val for val in values if val!=d])')
#         
#         elif des.name == 'vertexAttrib':
#             for i in (1,2,3,4):
#                 args = ', '.join(['v%i'%j for j in range(1,i+1)])
#                 sig = '%if(index, %s)' % (i, args)
#                 lines.append('def vertexAttrib%s:' % sig)
#                 lines.append('    _lib.glVertexAttrib%s' % sig)
#         elif des.name == 'getVertexAttrib':
#             for t in ('float', 'int'):
#                 lines.append('def getVertexAttrib%sv(index, pname):' % t[0])
#                 lines.append('    d = -99999  # Note: this is a bit dangerous')
#                 lines.append('    values = (ctypes.c_%s*4)(*[d for i in range(4)])' % t)
#                 lines.append('    _lib.glGetVertexAttrib%sv(index, pname, values)' % t[0])
#                 lines.append('    return tuple([val for val in values if val!=d])')
#         
#         elif des.name == 'texParameter':
#             for t in ('float', 'int'):
#                 lines.append('def texParameter%s(target, pname, param):' % t[0])
#                 lines.append('    _lib.glTexParameter%s(target, pname, param)' % t[0])
#         elif des.name == 'getTexParameter':
#             for t in ('float', 'int'):
#                 lines.append('def getTexParameter%sv(target, pname):' % t[0])
#                 lines.append('    params = (ctypes.c_%s*1)()')
#                 lines.append('    _lib.glGetTexParameter%sv(target, pname, params)' % t[0])
#                 lines.append('    return params[0]')
#         
#         else:
#             handled = False
#         
#         if handled:
#             functions_auto.add(des.name)
#         else:
#             functions_todo.add(des.name)
#             lines.append('# todo: Dont know group %s' % des.name)



class AngleApiGenrator(DesktopApiGenerator):
    filename = os.path.join(GLDIR, '_angle.py')
    write_c_sig = True
    
    PREAMBLE = """
    import ctypes.util
    fname = ctypes.util.find_library('gles')
    _lib = ctypes.cdll.LoadLibrary(fname)
    """



## Generate

# Get functions
functions = combine_function_definitions()

# Generate
for Gen in [MainApiGenerator, DesktopApiGenerator, AngleApiGenrator, CompatApiGenrator]:
    gen = Gen()
    for des in functions:
        gen.add_function(des)
    gen.save()


## Reporting

# Check which WebGL functions we did not find/use
for name in set(parser2.function_names).difference(used_webgl_names):
    print('WARNING: WebGL function %s not in Desktop' % name)

# Report status
print('Could generate %i functions automatically, and %i with annotations' %
      (len(functions_auto), len(functions_anno)))
print('Need more info for %i functions.' % len(functions_todo))
if not functions_todo:
    print('Hooray! All %i functions are covered!' % len(functions))
