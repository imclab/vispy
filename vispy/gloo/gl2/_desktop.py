"""

THIS CODE IS AUTO-GENERATED. DO NOT EDIT.

GL API X

"""

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

# void = glActiveTexture(GLenum texture)
def activeTexture(texture):
    try:
        func = activeTexture._native
    except AttributeError:
        func = activeTexture._native = _get_gl_func("glActiveTexture", None, (ctypes.c_uint,))
    func(texture)


# void = glAttachShader(GLuint program, GLuint shader)
def attachShader(program, shader):
    try:
        func = attachShader._native
    except AttributeError:
        func = attachShader._native = _get_gl_func("glAttachShader", None, (ctypes.c_uint, ctypes.c_uint,))
    func(program, shader)


# void = glBindAttribLocation(GLuint program, GLuint index, GLchar* name)
def bindAttribLocation(program, index, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    try:
        func = bindAttribLocation._native
    except AttributeError:
        func = bindAttribLocation._native = _get_gl_func("glBindAttribLocation", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_char_p,))
    res = func(program, index, name)


# void = glBindBuffer(GLenum target, GLuint buffer)
def bindBuffer(target, buffer):
    try:
        func = bindBuffer._native
    except AttributeError:
        func = bindBuffer._native = _get_gl_func("glBindBuffer", None, (ctypes.c_uint, ctypes.c_uint,))
    func(target, buffer)


# void = glBindFramebuffer(GLenum target, GLuint framebuffer)
def bindFramebuffer(target, framebuffer):
    try:
        func = bindFramebuffer._native
    except AttributeError:
        func = bindFramebuffer._native = _get_gl_func("glBindFramebuffer", None, (ctypes.c_uint, ctypes.c_uint,))
    func(target, framebuffer)


# void = glBindRenderbuffer(GLenum target, GLuint renderbuffer)
def bindRenderbuffer(target, renderbuffer):
    try:
        func = bindRenderbuffer._native
    except AttributeError:
        func = bindRenderbuffer._native = _get_gl_func("glBindRenderbuffer", None, (ctypes.c_uint, ctypes.c_uint,))
    func(target, renderbuffer)


# void = glBindTexture(GLenum target, GLuint texture)
def bindTexture(target, texture):
    try:
        func = bindTexture._native
    except AttributeError:
        func = bindTexture._native = _get_gl_func("glBindTexture", None, (ctypes.c_uint, ctypes.c_uint,))
    func(target, texture)


# void = glBlendColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
def blendColor(red, green, blue, alpha):
    try:
        func = blendColor._native
    except AttributeError:
        func = blendColor._native = _get_gl_func("glBlendColor", None, (ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
    func(red, green, blue, alpha)


# void = glBlendEquation(GLenum mode)
def blendEquation(mode):
    try:
        func = blendEquation._native
    except AttributeError:
        func = blendEquation._native = _get_gl_func("glBlendEquation", None, (ctypes.c_uint,))
    func(mode)


# void = glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha)
def blendEquationSeparate(modeRGB, modeAlpha):
    try:
        func = blendEquationSeparate._native
    except AttributeError:
        func = blendEquationSeparate._native = _get_gl_func("glBlendEquationSeparate", None, (ctypes.c_uint, ctypes.c_uint,))
    func(modeRGB, modeAlpha)


# void = glBlendFunc(GLenum sfactor, GLenum dfactor)
def blendFunc(sfactor, dfactor):
    try:
        func = blendFunc._native
    except AttributeError:
        func = blendFunc._native = _get_gl_func("glBlendFunc", None, (ctypes.c_uint, ctypes.c_uint,))
    func(sfactor, dfactor)


# void = glBlendFuncSeparate(GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
def blendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha):
    try:
        func = blendFuncSeparate._native
    except AttributeError:
        func = blendFuncSeparate._native = _get_gl_func("glBlendFuncSeparate", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
    func(srcRGB, dstRGB, srcAlpha, dstAlpha)


# void = glBufferData(GLenum target, GLsizeiptr size, GLvoid* data, GLenum usage)
def bufferData(target, data, usage):
    """ Data can be numpy array or the size of data to allocate.
    """
    if isinstance(data, int):
        size = data
        data = ctypes.c_voidp(0)
    else:
        if not data.flags['C_CONTIGUOUS'] or not data.flags['ALIGNED']:
            data = data.copy('C')
        data_ = data
        size = data_.nbytes
        data = data_.ctypes.data
    try:
        func = bufferData._native
    except AttributeError:
        func = bufferData._native = _get_gl_func("glBufferData", None, (ctypes.c_uint, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_uint,))
    res = func(target, size, data, usage)


# void = glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, GLvoid* data)
def bufferSubData(target, offset, data):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.nbytes
    data = data_.ctypes.data
    try:
        func = bufferSubData._native
    except AttributeError:
        func = bufferSubData._native = _get_gl_func("glBufferSubData", None, (ctypes.c_uint, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p,))
    res = func(target, offset, size, data)


# GLenum = glCheckFramebufferStatus(GLenum target)
def checkFramebufferStatus(target):
    try:
        func = checkFramebufferStatus._native
    except AttributeError:
        func = checkFramebufferStatus._native = _get_gl_func("glCheckFramebufferStatus", ctypes.c_uint, (ctypes.c_uint,))
    return func(target)


# void = glClear(GLbitfield mask)
def clear(mask):
    try:
        func = clear._native
    except AttributeError:
        func = clear._native = _get_gl_func("glClear", None, (ctypes.c_uint,))
    func(mask)


# void = glClearColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
def clearColor(red, green, blue, alpha):
    try:
        func = clearColor._native
    except AttributeError:
        func = clearColor._native = _get_gl_func("glClearColor", None, (ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
    func(red, green, blue, alpha)


# void = glClearDepthf(GLclampf depth)
def clearDepthf(depth):
    try:
        func = clearDepthf._native
    except AttributeError:
        func = clearDepthf._native = _get_gl_func("glClearDepthf", None, (ctypes.c_float,))
    func(depth)


# void = glClearStencil(GLint s)
def clearStencil(s):
    try:
        func = clearStencil._native
    except AttributeError:
        func = clearStencil._native = _get_gl_func("glClearStencil", None, (ctypes.c_int,))
    func(s)


# void = glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
def colorMask(red, green, blue, alpha):
    try:
        func = colorMask._native
    except AttributeError:
        func = colorMask._native = _get_gl_func("glColorMask", None, (ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool,))
    func(red, green, blue, alpha)


# void = glCompileShader(GLuint shader)
def compileShader(shader):
    try:
        func = compileShader._native
    except AttributeError:
        func = compileShader._native = _get_gl_func("glCompileShader", None, (ctypes.c_uint,))
    func(shader)


# void = glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, GLvoid* data)
def compressedTexImage2D(target, level, internalformat, width=0, height=0, border=0, data=None):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.size
    data = data_.ctypes.data
    try:
        func = compressedTexImage2D._native
    except AttributeError:
        func = compressedTexImage2D._native = _get_gl_func("glCompressedTexImage2D", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p,))
    res = func(target, level, internalformat, width, height, border, imageSize, data)


# void = glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, GLvoid* data)
def compressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.size
    data = data_.ctypes.data
    try:
        func = compressedTexSubImage2D._native
    except AttributeError:
        func = compressedTexSubImage2D._native = _get_gl_func("glCompressedTexSubImage2D", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p,))
    res = func(target, level, xoffset, yoffset, width, height, format, imageSize, data)


# void = glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
def copyTexImage2D(target, level, internalformat, x, y, width, height, border):
    try:
        func = copyTexImage2D._native
    except AttributeError:
        func = copyTexImage2D._native = _get_gl_func("glCopyTexImage2D", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(target, level, internalformat, x, y, width, height, border)


# void = glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
def copyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    try:
        func = copyTexSubImage2D._native
    except AttributeError:
        func = copyTexSubImage2D._native = _get_gl_func("glCopyTexSubImage2D", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(target, level, xoffset, yoffset, x, y, width, height)


# GLuint = glCreateProgram()
def createProgram():
    try:
        func = createProgram._native
    except AttributeError:
        func = createProgram._native = _get_gl_func("glCreateProgram", ctypes.c_uint, ())
    return func()


# GLuint = glCreateShader(GLenum type)
def createShader(type):
    try:
        func = createShader._native
    except AttributeError:
        func = createShader._native = _get_gl_func("glCreateShader", ctypes.c_uint, (ctypes.c_uint,))
    return func(type)


# void = glCullFace(GLenum mode)
def cullFace(mode):
    try:
        func = cullFace._native
    except AttributeError:
        func = cullFace._native = _get_gl_func("glCullFace", None, (ctypes.c_uint,))
    func(mode)


# void = glDeleteBuffers(GLsizei n, GLuint* buffers)
def deleteBuffer(buffer):
    n = 1
    buffers = (ctypes.c_uint*n)(buffer)
    try:
        func = deleteBuffer._native
    except AttributeError:
        func = deleteBuffer._native = _get_gl_func("glDeleteBuffers", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, buffers)


# void = glDeleteFramebuffers(GLsizei n, GLuint* framebuffers)
def deleteFramebuffer(framebuffer):
    n = 1
    buffers = (ctypes.c_uint*n)(framebuffer)
    try:
        func = deleteFramebuffer._native
    except AttributeError:
        func = deleteFramebuffer._native = _get_gl_func("glDeleteFramebuffers", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, framebuffers)


# void = glDeleteProgram(GLuint program)
def deleteProgra(program):
    try:
        func = deleteProgra._native
    except AttributeError:
        func = deleteProgra._native = _get_gl_func("glDeleteProgram", None, (ctypes.c_uint,))
    func(program)


# void = glDeleteRenderbuffers(GLsizei n, GLuint* renderbuffers)
def deleteRenderbuffer(renderbuffer):
    n = 1
    buffers = (ctypes.c_uint*n)(renderbuffer)
    try:
        func = deleteRenderbuffer._native
    except AttributeError:
        func = deleteRenderbuffer._native = _get_gl_func("glDeleteRenderbuffers", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, renderbuffers)


# void = glDeleteShader(GLuint shader)
def deleteShade(shader):
    try:
        func = deleteShade._native
    except AttributeError:
        func = deleteShade._native = _get_gl_func("glDeleteShader", None, (ctypes.c_uint,))
    func(shader)


# void = glDeleteTextures(GLsizei n, GLuint* textures)
def deleteTexture(texture):
    n = 1
    buffers = (ctypes.c_uint*n)(texture)
    try:
        func = deleteTexture._native
    except AttributeError:
        func = deleteTexture._native = _get_gl_func("glDeleteTextures", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, textures)


# void = glDepthFunc(GLenum func)
def depthFunc(func):
    try:
        func = depthFunc._native
    except AttributeError:
        func = depthFunc._native = _get_gl_func("glDepthFunc", None, (ctypes.c_uint,))
    func(func)


# void = glDepthMask(GLboolean flag)
def depthMask(flag):
    try:
        func = depthMask._native
    except AttributeError:
        func = depthMask._native = _get_gl_func("glDepthMask", None, (ctypes.c_bool,))
    func(flag)


# void = glDepthRangef(GLclampf zNear, GLclampf zFar)
def depthRangef(zNear, zFar):
    try:
        func = depthRangef._native
    except AttributeError:
        func = depthRangef._native = _get_gl_func("glDepthRangef", None, (ctypes.c_float, ctypes.c_float,))
    func(zNear, zFar)


# void = glDetachShader(GLuint program, GLuint shader)
def detachShader(program, shader):
    try:
        func = detachShader._native
    except AttributeError:
        func = detachShader._native = _get_gl_func("glDetachShader", None, (ctypes.c_uint, ctypes.c_uint,))
    func(program, shader)


# void = glDisable(GLenum cap)
def disable(cap):
    try:
        func = disable._native
    except AttributeError:
        func = disable._native = _get_gl_func("glDisable", None, (ctypes.c_uint,))
    func(cap)


# void = glDisableVertexAttribArray(GLuint index)
def disableVertexAttribArray(index):
    try:
        func = disableVertexAttribArray._native
    except AttributeError:
        func = disableVertexAttribArray._native = _get_gl_func("glDisableVertexAttribArray", None, (ctypes.c_uint,))
    func(index)


# void = glDrawArrays(GLenum mode, GLint first, GLsizei count)
def drawArrays(mode, first, count):
    try:
        func = drawArrays._native
    except AttributeError:
        func = drawArrays._native = _get_gl_func("glDrawArrays", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_int,))
    func(mode, first, count)


# void = glDrawElements(GLenum mode, GLsizei count, GLenum type, GLvoid* indices)
def drawElements(mode, count, type, offset):
    """ offset can be integer offset or array of indices.
    """
    if offset is None:
        offset = ctypes.c_void_p(0)
    elif isinstance(offset, c_void_p):
        pass
    elif isinstance(offset, (int, ctypes.c_int)):
        offset = ctypes.c_void_p(int(offset))
    else:
        if not offset.flags['C_CONTIGUOUS']:
            offset = offset.copy('C')
        offset_ = offset
        offset = offset.ctypes.data
    indices = offset
    try:
        func = drawElements._native
    except AttributeError:
        func = drawElements._native = _get_gl_func("glDrawElements", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p,))
    res = func(mode, count, type, indices)


# void = glEnable(GLenum cap)
def enable(cap):
    try:
        func = enable._native
    except AttributeError:
        func = enable._native = _get_gl_func("glEnable", None, (ctypes.c_uint,))
    func(cap)


# void = glEnableVertexAttribArray(GLuint index)
def enableVertexAttribArray(index):
    try:
        func = enableVertexAttribArray._native
    except AttributeError:
        func = enableVertexAttribArray._native = _get_gl_func("glEnableVertexAttribArray", None, (ctypes.c_uint,))
    func(index)


# void = glFinish()
def finish():
    try:
        func = finish._native
    except AttributeError:
        func = finish._native = _get_gl_func("glFinish", None, ())
    func()


# void = glFlush()
def flush():
    try:
        func = flush._native
    except AttributeError:
        func = flush._native = _get_gl_func("glFlush", None, ())
    func()


# void = glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
def framebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
    try:
        func = framebufferRenderbuffer._native
    except AttributeError:
        func = framebufferRenderbuffer._native = _get_gl_func("glFramebufferRenderbuffer", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
    func(target, attachment, renderbuffertarget, renderbuffer)


# void = glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
def framebufferTexture2D(target, attachment, textarget, texture, level):
    try:
        func = framebufferTexture2D._native
    except AttributeError:
        func = framebufferTexture2D._native = _get_gl_func("glFramebufferTexture2D", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_int,))
    func(target, attachment, textarget, texture, level)


# void = glFrontFace(GLenum mode)
def frontFace(mode):
    try:
        func = frontFace._native
    except AttributeError:
        func = frontFace._native = _get_gl_func("glFrontFace", None, (ctypes.c_uint,))
    func(mode)


# void = glGenBuffers(GLsizei n, GLuint* buffers)
def createBuffer():
    n = 1
    buffers = (ctypes.c_uint*n)()
    try:
        func = createBuffer._native
    except AttributeError:
        func = createBuffer._native = _get_gl_func("glGenBuffers", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, buffers)
    return buffers[0]


# void = glGenFramebuffers(GLsizei n, GLuint* framebuffers)
def createFramebuffer():
    n = 1
    framebuffers = (ctypes.c_uint*n)()
    try:
        func = createFramebuffer._native
    except AttributeError:
        func = createFramebuffer._native = _get_gl_func("glGenFramebuffers", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, framebuffers)
    return framebuffers[0]


# void = glGenRenderbuffers(GLsizei n, GLuint* renderbuffers)
def createRenderbuffer():
    n = 1
    renderbuffers = (ctypes.c_uint*n)()
    try:
        func = createRenderbuffer._native
    except AttributeError:
        func = createRenderbuffer._native = _get_gl_func("glGenRenderbuffers", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, renderbuffers)
    return renderbuffers[0]


# void = glGenTextures(GLsizei n, GLuint* textures)
def createTexture():
    n = 1
    textures = (ctypes.c_uint*n)()
    try:
        func = createTexture._native
    except AttributeError:
        func = createTexture._native = _get_gl_func("glGenTextures", None, (ctypes.c_int, ctypes.POINTER(ctypes.c_uint),))
    res = func(n, textures)
    return textures[0]


# void = glGenerateMipmap(GLenum target)
def createerateMipma(target):
    try:
        func = createerateMipma._native
    except AttributeError:
        func = createerateMipma._native = _get_gl_func("glGenerateMipmap", None, (ctypes.c_uint,))
    func(target)


# void = glGetActiveAttrib(GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name)
def getActiveAttrib(program, index):
    bufsize = 256
    length = (ctypes.c_int*1)()
    size = (ctypes.c_int*1)()
    type = (ctypes.c_uint*1)()
    name = ctypes.create_string_buffer(bufsize)
    try:
        func = getActiveAttrib._native
    except AttributeError:
        func = getActiveAttrib._native = _get_gl_func("glGetActiveAttrib", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p,))
    res = func(program, index, bufsize, length, size, type, name)
    name = name[:length[0]].decode('utf-8')
    return name, size[0], type[0]


# void = glGetActiveUniform(GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name)
def getActiveUniform(program, index):
    bufsize = 256
    length = (ctypes.c_int*1)()
    size = (ctypes.c_int*1)()
    type = (ctypes.c_uint*1)()
    name = ctypes.create_string_buffer(bufsize)
    try:
        func = getActiveUniform._native
    except AttributeError:
        func = getActiveUniform._native = _get_gl_func("glGetActiveUniform", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p,))
    res = func(program, index, bufsize, length, size, type, name)
    name = name[:length[0]].decode('utf-8')
    return name, size[0], type[0]


# void = glGetAttachedShaders(GLuint program, GLsizei maxcount, GLsizei* count, GLuint* shaders)
def getAttachedShaders(program):
    maxcount = 256
    count = (ctypes.c_int*1)()
    shaders = (ctypes.c_uint*1)()
    try:
        func = getAttachedShaders._native
    except AttributeError:
        func = getAttachedShaders._native = _get_gl_func("glGetAttachedShaders", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint),))
    res = func(program, maxcount, count, shaders)
    return tuple(shaders[:count[0]])


# GLint = glGetAttribLocation(GLuint program, GLchar* name)
def getAttribLocation(program, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    try:
        func = getAttribLocation._native
    except AttributeError:
        func = getAttribLocation._native = _get_gl_func("glGetAttribLocation", ctypes.c_int, (ctypes.c_uint, ctypes.c_char_p,))
    res = func(program, name)
    return res


# void = glGetBooleanv(GLenum pname, GLboolean* params)
def getBooleanv(pname):
    data = (ctypes.c_bool*1)()
    try:
        func = getBooleanv._native
    except AttributeError:
        func = getBooleanv._native = _get_gl_func("glGetBooleanv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_bool),))
    res = func(pname, params)
    return data[0]


# void = glGetBufferParameteriv(GLenum target, GLenum pname, GLint* params)
def getBufferParameteriv(target, pname):
    data = (ctypes.c_int*1)()
    try:
        func = getBufferParameteriv._native
    except AttributeError:
        func = getBufferParameteriv._native = _get_gl_func("glGetBufferParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    res = func(target, pname, params)
    return data[0]


# GLenum = glGetError()
def getError():
    try:
        func = getError._native
    except AttributeError:
        func = getError._native = _get_gl_func("glGetError", ctypes.c_uint, ())
    return func()


# void = glGetFloatv(GLenum pname, GLfloat* params)
def getFloatv(pname):
    data = (ctypes.c_float*1)()
    try:
        func = getFloatv._native
    except AttributeError:
        func = getFloatv._native = _get_gl_func("glGetFloatv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
    res = func(pname, params)
    return data[0]


# void = glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname, GLint* params)
def getFramebufferAttachmentParameteriv(target, attachment, pname):
    params = (ctypes.c_int*1)()
    try:
        func = getFramebufferAttachmentParameteriv._native
    except AttributeError:
        func = getFramebufferAttachmentParameteriv._native = _get_gl_func("glGetFramebufferAttachmentParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    res = func(target, attachment, pname, params)
    return params[0]


# void = glGetIntegerv(GLenum pname, GLint* params)
def getIntegerv(pname):
    data = (ctypes.c_int*1)()
    try:
        func = getIntegerv._native
    except AttributeError:
        func = getIntegerv._native = _get_gl_func("glGetIntegerv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    res = func(pname, params)
    return data[0]


# void = glGetProgramInfoLog(GLuint program, GLsizei bufsize, GLsizei* length, GLchar* infolog)
def getProgramInfoLog(program):
    bufsize = 1024
    length = (ctypes.c_int*1)()
    infolog = ctypes.create_string_buffer(bufsize)
    try:
        func = getProgramInfoLog._native
    except AttributeError:
        func = getProgramInfoLog._native = _get_gl_func("glGetProgramInfoLog", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p,))
    res = func(program, bufsize, length, infolog)
    return infolog[:length[0]].decode('utf-8')


# void = glGetProgramiv(GLuint program, GLenum pname, GLint* params)
def getProgramiv(program, pname):
    params = (ctypes.c_int*1)()
    try:
        func = getProgramiv._native
    except AttributeError:
        func = getProgramiv._native = _get_gl_func("glGetProgramiv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    res = func(program, pname, params)
    return params[0]


# void = glGetRenderbufferParameteriv(GLenum target, GLenum pname, GLint* params)
def getRenderbufferParameteriv(target, pname):
    params = (ctypes.c_int*1)()
    try:
        func = getRenderbufferParameteriv._native
    except AttributeError:
        func = getRenderbufferParameteriv._native = _get_gl_func("glGetRenderbufferParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    res = func(target, pname, params)
    return params[0]


# void = glGetShaderInfoLog(GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* infolog)
def getShaderInfoLog(shader):
    bufsize = 1024
    length = (ctypes.c_int*1)()
    infolog = ctypes.create_string_buffer(bufsize)
    try:
        func = getShaderInfoLog._native
    except AttributeError:
        func = getShaderInfoLog._native = _get_gl_func("glGetShaderInfoLog", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p,))
    res = func(shader, bufsize, length, infolog)
    return infolog[:length[0]].decode('utf-8')


# void = glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint* range, GLint* precision)
def getShaderPrecisionFormat(shadertype, precisiontype):
    range = (ctypes.c_int*1)()
    precision = (ctypes.c_int*1)()
    try:
        func = getShaderPrecisionFormat._native
    except AttributeError:
        func = getShaderPrecisionFormat._native = _get_gl_func("glGetShaderPrecisionFormat", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),))
    res = func(shadertype, precisiontype, range, precision)
    return range[0], precision[0]


# void = glGetShaderSource(GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* source)
def getShaderSource(shader):
    bufSize = 1024*1024
    length = (ctypes.c_int*1)()
    source = (ctypes.c_char*bufsize)()
    try:
        func = getShaderSource._native
    except AttributeError:
        func = getShaderSource._native = _get_gl_func("glGetShaderSource", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p,))
    res = func(shader, bufsize, length, source)
    return source.value[:length[0]].decode('utf-8')


# void = glGetShaderiv(GLuint shader, GLenum pname, GLint* params)
def getShaderiv(shader, pname):
    params = (ctypes.c_int*1)()
    try:
        func = getShaderiv._native
    except AttributeError:
        func = getShaderiv._native = _get_gl_func("glGetShaderiv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    res = func(shader, pname, params)
    return params[0]


# GLubyte* = glGetString(GLenum name)
def getString(pname):
    try:
        func = getString._native
    except AttributeError:
        func = getString._native = _get_gl_func("glGetString", ctypes.c_char_p, (ctypes.c_uint,))
    res = func(name)
    return res.value


def getTexParameterfv(target, pname):
    params = (ctypes.c_float*1)()
    try:
        func = getTexParameterfv._native
    except AttributeError:
        func = getTexParameterfv._native = _get_gl_func("glGetTexParameterfv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
    func(target, pname, params)
    return params[0]
def getTexParameteriv(target, pname):
    params = (ctypes.c_int*1)()
    try:
        func = getTexParameteriv._native
    except AttributeError:
        func = getTexParameteriv._native = _get_gl_func("glGetTexParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    func(target, pname, params)
    return params[0]


def getUniformfv(program, location):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_float*16)(*[d for i in range(16)])
    try:
        func = getUniformfv._native
    except AttributeError:
        func = getUniformfv._native = _get_gl_func("glGetUniformfv", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float),))
    func(program, location, values)
    return tuple([val for val in values if val!=d])
def getUniformiv(program, location):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_int*16)(*[d for i in range(16)])
    try:
        func = getUniformiv._native
    except AttributeError:
        func = getUniformiv._native = _get_gl_func("glGetUniformiv", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int),))
    func(program, location, values)
    return tuple([val for val in values if val!=d])


# GLint = glGetUniformLocation(GLuint program, GLchar* name)
def getUniformLocation(program, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    try:
        func = getUniformLocation._native
    except AttributeError:
        func = getUniformLocation._native = _get_gl_func("glGetUniformLocation", ctypes.c_int, (ctypes.c_uint, ctypes.c_char_p,))
    res = func(program, name)
    return res


def getVertexAttribfv(index, pname):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_float*4)(*[d for i in range(4)])
    try:
        func = getVertexAttribfv._native
    except AttributeError:
        func = getVertexAttribfv._native = _get_gl_func("glGetVertexAttribfv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
    func(index, pname, values)
    return tuple([val for val in values if val!=d])
def getVertexAttribiv(index, pname):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_int*4)(*[d for i in range(4)])
    try:
        func = getVertexAttribiv._native
    except AttributeError:
        func = getVertexAttribiv._native = _get_gl_func("glGetVertexAttribiv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),))
    func(index, pname, values)
    return tuple([val for val in values if val!=d])


# void = glGetVertexAttribPointerv(GLuint index, GLenum pname, GLvoid** pointer)
def getVertexAttribPointerv(index, pname):
    pointer = (ctypes.c_void_p*1)()
    try:
        func = getVertexAttribPointerv._native
    except AttributeError:
        func = getVertexAttribPointerv._native = _get_gl_func("glGetVertexAttribPointerv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_void_p),))
    res = func(index, pname, pointer)
    return pointer[0]


# void = glHint(GLenum target, GLenum mode)
def hint(target, mode):
    try:
        func = hint._native
    except AttributeError:
        func = hint._native = _get_gl_func("glHint", None, (ctypes.c_uint, ctypes.c_uint,))
    func(target, mode)


# GLboolean = glIsBuffer(GLuint buffer)
def isBuffer(buffer):
    try:
        func = isBuffer._native
    except AttributeError:
        func = isBuffer._native = _get_gl_func("glIsBuffer", ctypes.c_bool, (ctypes.c_uint,))
    return func(buffer)


# GLboolean = glIsEnabled(GLenum cap)
def isEnabled(cap):
    try:
        func = isEnabled._native
    except AttributeError:
        func = isEnabled._native = _get_gl_func("glIsEnabled", ctypes.c_bool, (ctypes.c_uint,))
    return func(cap)


# GLboolean = glIsFramebuffer(GLuint framebuffer)
def isFramebuffer(framebuffer):
    try:
        func = isFramebuffer._native
    except AttributeError:
        func = isFramebuffer._native = _get_gl_func("glIsFramebuffer", ctypes.c_bool, (ctypes.c_uint,))
    return func(framebuffer)


# GLboolean = glIsProgram(GLuint program)
def isProgram(program):
    try:
        func = isProgram._native
    except AttributeError:
        func = isProgram._native = _get_gl_func("glIsProgram", ctypes.c_bool, (ctypes.c_uint,))
    return func(program)


# GLboolean = glIsRenderbuffer(GLuint renderbuffer)
def isRenderbuffer(renderbuffer):
    try:
        func = isRenderbuffer._native
    except AttributeError:
        func = isRenderbuffer._native = _get_gl_func("glIsRenderbuffer", ctypes.c_bool, (ctypes.c_uint,))
    return func(renderbuffer)


# GLboolean = glIsShader(GLuint shader)
def isShader(shader):
    try:
        func = isShader._native
    except AttributeError:
        func = isShader._native = _get_gl_func("glIsShader", ctypes.c_bool, (ctypes.c_uint,))
    return func(shader)


# GLboolean = glIsTexture(GLuint texture)
def isTexture(texture):
    try:
        func = isTexture._native
    except AttributeError:
        func = isTexture._native = _get_gl_func("glIsTexture", ctypes.c_bool, (ctypes.c_uint,))
    return func(texture)


# void = glLineWidth(GLfloat width)
def lineWidth(width):
    try:
        func = lineWidth._native
    except AttributeError:
        func = lineWidth._native = _get_gl_func("glLineWidth", None, (ctypes.c_float,))
    func(width)


# void = glLinkProgram(GLuint program)
def linkProgram(program):
    try:
        func = linkProgram._native
    except AttributeError:
        func = linkProgram._native = _get_gl_func("glLinkProgram", None, (ctypes.c_uint,))
    func(program)


# void = glPixelStorei(GLenum pname, GLint param)
def pixelStorei(pname, param):
    try:
        func = pixelStorei._native
    except AttributeError:
        func = pixelStorei._native = _get_gl_func("glPixelStorei", None, (ctypes.c_uint, ctypes.c_int,))
    func(pname, param)


# void = glPolygonOffset(GLfloat factor, GLfloat units)
def polygonOffset(factor, units):
    try:
        func = polygonOffset._native
    except AttributeError:
        func = polygonOffset._native = _get_gl_func("glPolygonOffset", None, (ctypes.c_float, ctypes.c_float,))
    func(factor, units)


# void = glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels)
def readPixels(x, y, width, height, format, type):
    """ Return pixels as bytes.
    """
    size = width*height
    pixels = (ctypes.c_uint8*size)()
    try:
        func = readPixels._native
    except AttributeError:
        func = readPixels._native = _get_gl_func("glReadPixels", None, (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,))
    res = func(x, y, width, height, format, type, pixels)
    return bytes(pixels)


# void = glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height)
def renderbufferStorage(target, internalformat, width, height):
    try:
        func = renderbufferStorage._native
    except AttributeError:
        func = renderbufferStorage._native = _get_gl_func("glRenderbufferStorage", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_int,))
    func(target, internalformat, width, height)


# void = glSampleCoverage(GLclampf value, GLboolean invert)
def sampleCoverage(value, invert):
    try:
        func = sampleCoverage._native
    except AttributeError:
        func = sampleCoverage._native = _get_gl_func("glSampleCoverage", None, (ctypes.c_float, ctypes.c_bool,))
    func(value, invert)


# void = glScissor(GLint x, GLint y, GLsizei width, GLsizei height)
def scissor(x, y, width, height):
    try:
        func = scissor._native
    except AttributeError:
        func = scissor._native = _get_gl_func("glScissor", None, (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(x, y, width, height)


# void = glShaderSource(GLuint shader, GLsizei count, GLchar** string, GLint* length)
def shaderSource(shader, *strings):
    if len(strings) == 1 and isinstance(strings[0], (tuple, list)):
        strings = strings[0]
    count = len(strings)
    string = (ctypes.c_char_p*count)(*[s.encode('utf-8') for s in strings])
    length = (ctypes.c_int*count)(*[len(s) for s in strings])
    try:
        func = shaderSource._native
    except AttributeError:
        func = shaderSource._native = _get_gl_func("glShaderSource", None, (ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int),))
    res = func(shader, count, string, length)


# void = glStencilFunc(GLenum func, GLint ref, GLuint mask)
def stencilFunc(func, ref, mask):
    try:
        func = stencilFunc._native
    except AttributeError:
        func = stencilFunc._native = _get_gl_func("glStencilFunc", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_uint,))
    func(func, ref, mask)


# void = glStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask)
def stencilFuncSeparate(face, func, ref, mask):
    try:
        func = stencilFuncSeparate._native
    except AttributeError:
        func = stencilFuncSeparate._native = _get_gl_func("glStencilFuncSeparate", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_uint,))
    func(face, func, ref, mask)


# void = glStencilMask(GLuint mask)
def stencilMask(mask):
    try:
        func = stencilMask._native
    except AttributeError:
        func = stencilMask._native = _get_gl_func("glStencilMask", None, (ctypes.c_uint,))
    func(mask)


# void = glStencilMaskSeparate(GLenum face, GLuint mask)
def stencilMaskSeparate(face, mask):
    try:
        func = stencilMaskSeparate._native
    except AttributeError:
        func = stencilMaskSeparate._native = _get_gl_func("glStencilMaskSeparate", None, (ctypes.c_uint, ctypes.c_uint,))
    func(face, mask)


# void = glStencilOp(GLenum fail, GLenum zfail, GLenum zpass)
def stencilOp(fail, zfail, zpass):
    try:
        func = stencilOp._native
    except AttributeError:
        func = stencilOp._native = _get_gl_func("glStencilOp", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
    func(fail, zfail, zpass)


# void = glStencilOpSeparate(GLenum face, GLenum fail, GLenum zfail, GLenum zpass)
def stencilOpSeparate(face, fail, zfail, zpass):
    try:
        func = stencilOpSeparate._native
    except AttributeError:
        func = stencilOpSeparate._native = _get_gl_func("glStencilOpSeparate", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
    func(face, fail, zfail, zpass)


# void = glTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, GLvoid* pixels)
def texImage2D(target, level, internalformat, format, type, pixels):
    if isinstance(pixels, (tuple, list)):
        width, height = pixels
        pixels = ctypes.c_void_p(0)
    else:
        if not pixels.flags['C_CONTIGUOUS']:
            pixels = pixels.copy('C')
        pixels_ = pixels
        pixels = pixels_.ctypes.data
        width, height = pixels_.shape[:2]
    border = 0
    try:
        func = texImage2D._native
    except AttributeError:
        func = texImage2D._native = _get_gl_func("glTexImage2D", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,))
    res = func(target, level, internalformat, width, height, border, format, type, pixels)


def texParameterf(target, pname, param):
    try:
        func = texParameterf._native
    except AttributeError:
        func = texParameterf._native = _get_gl_func("glTexParameterf", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_float,))
    func(target, pname, param)
def texParameteri(target, pname, param):
    try:
        func = texParameteri._native
    except AttributeError:
        func = texParameteri._native = _get_gl_func("glTexParameteri", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_int,))
    func(target, pname, param)


# void = glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels)
def texSubImage2D(target, level, xoffset, yoffset, format, type, pixels):
    if not pixels.flags['C_CONTIGUOUS']:
        pixels = pixels.copy('C')
    pixels_ = pixels
    pixels = pixels_.ctypes.data
    width, height = pixels_.shape[:2]
    try:
        func = texSubImage2D._native
    except AttributeError:
        func = texSubImage2D._native = _get_gl_func("glTexSubImage2D", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,))
    res = func(target, level, xoffset, yoffset, width, height, format, type, pixels)


def uniform1f(location, v1):
    try:
        func = uniform1f._native
    except AttributeError:
        func = uniform1f._native = _get_gl_func("glUniform1f", None, (ctypes.c_int, ctypes.c_float,))
    func(location, v1)
def uniform2f(location, v1, v2):
    try:
        func = uniform2f._native
    except AttributeError:
        func = uniform2f._native = _get_gl_func("glUniform2f", None, (ctypes.c_int, ctypes.c_float, ctypes.c_float,))
    func(location, v1, v2)
def uniform3f(location, v1, v2, v3):
    try:
        func = uniform3f._native
    except AttributeError:
        func = uniform3f._native = _get_gl_func("glUniform3f", None, (ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
    func(location, v1, v2, v3)
def uniform4f(location, v1, v2, v3, v4):
    try:
        func = uniform4f._native
    except AttributeError:
        func = uniform4f._native = _get_gl_func("glUniform4f", None, (ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
    func(location, v1, v2, v3, v4)
def uniform1i(location, v1):
    try:
        func = uniform1i._native
    except AttributeError:
        func = uniform1i._native = _get_gl_func("glUniform1i", None, (ctypes.c_int, ctypes.c_int,))
    func(location, v1)
def uniform2i(location, v1, v2):
    try:
        func = uniform2i._native
    except AttributeError:
        func = uniform2i._native = _get_gl_func("glUniform2i", None, (ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(location, v1, v2)
def uniform3i(location, v1, v2, v3):
    try:
        func = uniform3i._native
    except AttributeError:
        func = uniform3i._native = _get_gl_func("glUniform3i", None, (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(location, v1, v2, v3)
def uniform4i(location, v1, v2, v3, v4):
    try:
        func = uniform4i._native
    except AttributeError:
        func = uniform4i._native = _get_gl_func("glUniform4i", None, (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(location, v1, v2, v3, v4)
def uniform1fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniform1fv._native
    except AttributeError:
        func = uniform1fv._native = _get_gl_func("glUniform1fv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),))
    func(location, count, values)
def uniform2fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniform2fv._native
    except AttributeError:
        func = uniform2fv._native = _get_gl_func("glUniform2fv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),))
    func(location, count, values)
def uniform3fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniform3fv._native
    except AttributeError:
        func = uniform3fv._native = _get_gl_func("glUniform3fv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),))
    func(location, count, values)
def uniform4fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniform4fv._native
    except AttributeError:
        func = uniform4fv._native = _get_gl_func("glUniform4fv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),))
    func(location, count, values)
def uniform1iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    try:
        func = uniform1iv._native
    except AttributeError:
        func = uniform1iv._native = _get_gl_func("glUniform1iv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),))
    func(location, count, values)
def uniform2iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    try:
        func = uniform2iv._native
    except AttributeError:
        func = uniform2iv._native = _get_gl_func("glUniform2iv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),))
    func(location, count, values)
def uniform3iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    try:
        func = uniform3iv._native
    except AttributeError:
        func = uniform3iv._native = _get_gl_func("glUniform3iv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),))
    func(location, count, values)
def uniform4iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    try:
        func = uniform4iv._native
    except AttributeError:
        func = uniform4iv._native = _get_gl_func("glUniform4iv", None, (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),))
    func(location, count, values)


def uniformMatrix2fv(location, count, transpose, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniformMatrix2fv._native
    except AttributeError:
        func = uniformMatrix2fv._native = _get_gl_func("glUniformMatrix2fv", None, (ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_float),))
    func(location, count, transpose, values)
def uniformMatrix3fv(location, count, transpose, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniformMatrix3fv._native
    except AttributeError:
        func = uniformMatrix3fv._native = _get_gl_func("glUniformMatrix3fv", None, (ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_float),))
    func(location, count, transpose, values)
def uniformMatrix4fv(location, count, transpose, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    try:
        func = uniformMatrix4fv._native
    except AttributeError:
        func = uniformMatrix4fv._native = _get_gl_func("glUniformMatrix4fv", None, (ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_float),))
    func(location, count, transpose, values)


# void = glUseProgram(GLuint program)
def useProgram(program):
    try:
        func = useProgram._native
    except AttributeError:
        func = useProgram._native = _get_gl_func("glUseProgram", None, (ctypes.c_uint,))
    func(program)


# void = glValidateProgram(GLuint program)
def validateProgram(program):
    try:
        func = validateProgram._native
    except AttributeError:
        func = validateProgram._native = _get_gl_func("glValidateProgram", None, (ctypes.c_uint,))
    func(program)


def vertexAttrib1f(index, v1):
    try:
        func = vertexAttrib1f._native
    except AttributeError:
        func = vertexAttrib1f._native = _get_gl_func("glVertexAttrib1f", None, (ctypes.c_uint, ctypes.c_float,))
    func(index, v1)
def vertexAttrib2f(index, v1, v2):
    try:
        func = vertexAttrib2f._native
    except AttributeError:
        func = vertexAttrib2f._native = _get_gl_func("glVertexAttrib2f", None, (ctypes.c_uint, ctypes.c_float, ctypes.c_float,))
    func(index, v1, v2)
def vertexAttrib3f(index, v1, v2, v3):
    try:
        func = vertexAttrib3f._native
    except AttributeError:
        func = vertexAttrib3f._native = _get_gl_func("glVertexAttrib3f", None, (ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
    func(index, v1, v2, v3)
def vertexAttrib4f(index, v1, v2, v3, v4):
    try:
        func = vertexAttrib4f._native
    except AttributeError:
        func = vertexAttrib4f._native = _get_gl_func("glVertexAttrib4f", None, (ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
    func(index, v1, v2, v3, v4)


# void = glVertexAttribPointer(GLuint indx, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLvoid* ptr)
def vertexAttribPointer(indx, size, type, normalized, stride, offset):
    if offset is None:
        offset = ctypes.c_void_p(0)
    elif isinstance(offset, ctypes.c_void_p):
        pass
    elif isinstance(offset, (int, ctypes.c_int)):
        offset = ctypes.c_void_p(int(offset))
    else:
        if not offset.flags['C_CONTIGUOUS']:
            offset = offset.copy('C')
        offset_ = offset
        offset = offset.ctypes.data
    ptr = offset
    try:
        func = vertexAttribPointer._native
    except AttributeError:
        func = vertexAttribPointer._native = _get_gl_func("glVertexAttribPointer", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_bool, ctypes.c_int, ctypes.c_void_p,))
    res = func(indx, size, type, normalized, stride, ptr)


# void = glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
def viewport(x, y, width, height):
    try:
        func = viewport._native
    except AttributeError:
        func = viewport._native = _get_gl_func("glViewport", None, (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,))
    func(x, y, width, height)


