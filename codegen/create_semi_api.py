

import os
import sys

import headerparser
from annotations import parse_anotations

from OpenGL import GL  # For checking

THISDIR = os.path.abspath(os.path.dirname(__file__))


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
print('All constants that occur in both namespaces have equal values.')




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
                        
                        'getVertexAttr': 'getVertexAttrib',
                        'getVertexAttribPointerv': 'getVertexAttribOffset',
                        
                        'getProgramiv': 'getProgramParameter',
                        'getShaderiv': 'getShaderParameter',
                        
                        'getBooleanv': 'getParameter',
                        'getFloatv': 'getParameter',
                        'getIntegerv': 'getParameter',
                        'getString': 'getParameter',
                    }


EASY_TYPES = {  'void': (type(None), 'c_voidp'),  # only for output
                'GLenum': (int, 'c_int'),
                'GLboolean': (bool, 'c_bool'),
                'GLuint': (int, 'c_uint'),
                'GLint': (int, 'c_int'),
                'GLbitfield': (int, 'c_uint'),
                'GLsizei': (int, 'c_int'),
                'GLfloat': (float, 'c_float'),
                'GLclampf': (float, 'c_float'),
             }


# Keep track of what webGL names we "used"
used_webgl_names = set()

# Also keep track of what functions we could handle automatically, 
# and which not. Just for reporting
functions_auto = []
functions_anno = []
functions_todo = []

# List of function argtypes
function_argtypes = []


# Process function definitions of ES 2.0
lines = []
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
    
    # Add line
    argnames = [arg.name for arg in es2func.args[1:]]
    argnamesstr = ', '.join(argnames)
    lines.append('def %s(%s):' % (es2func.pname, argnamesstr))
    argtypes = [EASY_TYPES.get(arg.ctype, None) for arg in es2func.args]
    # 
    if es2func.pname in annotations:
        functions_anno.append(es2func.pname)
        anno = annotations[es2func.pname]
        # Get args
        cargstr = ', '.join(argnames)
        pargstr = ', '.join(anno.args)
        callline = '%s_lib.%s(%s)' % (prefix, es2func.glname, cargstr)
        for line in anno.get_lines(callline, 'desktop'):
            lines.append('    '+line)
        # todo: Set argtypes
        
    elif es2func.group:
        functions_todo.append(es2func.pname)
        lines.append('    # todo: This is a group')
    elif None in argtypes:
        functions_todo.append(es2func.pname)
        lines.append('    # todo: Not all easy types!')
    elif wglfunc and argnames != [arg.name for arg in wglfunc.args[1:]]:
        functions_todo.append(es2func.pname)
        lines.append('    # todo: ES 2.0 and WebGL args do not match!')
    else:
        functions_auto.append(es2func.pname)
        # Get prefix
        prefix = ''
        if argtypes[0][0] != type(None):
            prefix = 'return '
        elif es2func.pname.startswith('get'):
            raise RuntimeError('Get func returns void?')
        # Set string
        argstr = ', '.join(argnames)
        #argstr = ', '.join(['%s(%s)' % (t[0].__name__, n) for (t,n) in zip(argtypes[1:], argnames)])
        lines.append('    %s_lib.%s(%s)' % (prefix, es2func.glname, argstr))
        # Set argtypes
        if argtypes[1:]:
            argstr = ', '.join(['ctypes.%s' % t[1] for t in argtypes[1:]])
            function_argtypes.append('_lib.%s.argtypes = %s,' % (es2func.glname, argstr))
        else:
            function_argtypes.append('_lib.%s.argtypes = ()' % es2func.glname)
    
    # Go over groups of ES 2.0 funcions
    for func in [es2func, wglfunc]:
        if func is None: 
            continue
        group = func.group or [func]
        for f in group:
            
            # Check opengl
            if f.oname.startswith('gl') and not hasattr(GL, f.glname):
                print('WARNING: %s seems not available in PyOpenGL' % f.pname)
            
            # Add line
            argnames = ['%s %s' % (arg.ctype, arg.name) for arg in f.args[1:]]
            argnamesstr = ', '.join(argnames)
            lines.append('    # %s = %s(%s)' % (f.args[0].ctype, f.oname, argnamesstr))
    
    # A line between each function
    lines.append('')


# Check which WebGL functions we did not find/use
for name in set(parser2.function_names).difference(used_webgl_names):
    print('WARNING: WebGL function %s not in Desktop' % name)

# Report status
print('Could generate %i functions automatically, and %i with annotations' %
      (len(functions_auto), len(functions_anno)))
print('Need more info for %i functions.' % len(functions_todo))

# Write file
with open('semi_api.py', 'wt') as f:
    for line in function_argtypes:
        f.write(line + '\n')
    f.write('\n\n')
    for line in lines:
        f.write(line + '\n')



