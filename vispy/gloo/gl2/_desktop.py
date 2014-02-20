"""

THIS CODE IS AUTO-GENERATED. DO NOT EDIT.

GL API X

"""

import ctypes.util
fname = ctypes.util.find_library('GL')
_lib = ctypes.cdll.LoadLibrary(fname)

_lib.glActiveTexture.argtypes = ctypes.c_uint,
# void = glActiveTexture(GLenum texture)
def activeTexture(texture):
    _lib.glActiveTexture(texture)


_lib.glAttachShader.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glAttachShader(GLuint program, GLuint shader)
def attachShader(program, shader):
    _lib.glAttachShader(program, shader)


_lib.glBindAttribLocation.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_char_p,
# void = glBindAttribLocation(GLuint program, GLuint index, GLchar* name)
def bindAttribLocation(program, index, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    res = _lib.glBindAttribLocation(program, index, name)


_lib.glBindBuffer.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glBindBuffer(GLenum target, GLuint buffer)
def bindBuffer(target, buffer):
    _lib.glBindBuffer(target, buffer)


_lib.glBindFramebuffer.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glBindFramebuffer(GLenum target, GLuint framebuffer)
def bindFramebuffer(target, framebuffer):
    _lib.glBindFramebuffer(target, framebuffer)


_lib.glBindRenderbuffer.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glBindRenderbuffer(GLenum target, GLuint renderbuffer)
def bindRenderbuffer(target, renderbuffer):
    _lib.glBindRenderbuffer(target, renderbuffer)


_lib.glBindTexture.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glBindTexture(GLenum target, GLuint texture)
def bindTexture(target, texture):
    _lib.glBindTexture(target, texture)


_lib.glBlendColor.argtypes = ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
# void = glBlendColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
def blendColor(red, green, blue, alpha):
    _lib.glBlendColor(red, green, blue, alpha)


_lib.glBlendEquation.argtypes = ctypes.c_uint,
# void = glBlendEquation(GLenum mode)
def blendEquation(mode):
    _lib.glBlendEquation(mode)


_lib.glBlendEquationSeparate.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha)
def blendEquationSeparate(modeRGB, modeAlpha):
    _lib.glBlendEquationSeparate(modeRGB, modeAlpha)


_lib.glBlendFunc.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glBlendFunc(GLenum sfactor, GLenum dfactor)
def blendFunc(sfactor, dfactor):
    _lib.glBlendFunc(sfactor, dfactor)


_lib.glBlendFuncSeparate.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,
# void = glBlendFuncSeparate(GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
def blendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha):
    _lib.glBlendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha)


_lib.glBufferData.argtypes = ctypes.c_uint, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_uint,
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
    res = _lib.glBufferData(target, size, data, usage)


_lib.glBufferSubData.argtypes = ctypes.c_uint, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p,
# void = glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, GLvoid* data)
def bufferSubData(target, offset, data):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.nbytes
    data = data_.ctypes.data
    res = _lib.glBufferSubData(target, offset, size, data)


_lib.glCheckFramebufferStatus.argtypes = ctypes.c_uint,
_lib.glCheckFramebufferStatus.restype = ctypes.c_uint
# GLenum = glCheckFramebufferStatus(GLenum target)
def checkFramebufferStatus(target):
    return _lib.glCheckFramebufferStatus(target)


_lib.glClear.argtypes = ctypes.c_uint,
# void = glClear(GLbitfield mask)
def clear(mask):
    _lib.glClear(mask)


_lib.glClearColor.argtypes = ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
# void = glClearColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
def clearColor(red, green, blue, alpha):
    _lib.glClearColor(red, green, blue, alpha)


_lib.glClearDepthf.argtypes = ctypes.c_float,
# void = glClearDepthf(GLclampf depth)
def clearDepthf(depth):
    _lib.glClearDepthf(depth)


_lib.glClearStencil.argtypes = ctypes.c_int,
# void = glClearStencil(GLint s)
def clearStencil(s):
    _lib.glClearStencil(s)


_lib.glColorMask.argtypes = ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool,
# void = glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
def colorMask(red, green, blue, alpha):
    _lib.glColorMask(red, green, blue, alpha)


_lib.glCompileShader.argtypes = ctypes.c_uint,
# void = glCompileShader(GLuint shader)
def compileShader(shader):
    _lib.glCompileShader(shader)


_lib.glCompressedTexImage2D.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p,
# void = glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, GLvoid* data)
def compressedTexImage2D(target, level, internalformat, width=0, height=0, border=0, data=None):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.size
    data = data_.ctypes.data
    res = _lib.glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)


_lib.glCompressedTexSubImage2D.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p,
# void = glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, GLvoid* data)
def compressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.size
    data = data_.ctypes.data
    res = _lib.glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)


_lib.glCopyTexImage2D.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
# void = glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
def copyTexImage2D(target, level, internalformat, x, y, width, height, border):
    _lib.glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)


_lib.glCopyTexSubImage2D.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
# void = glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
def copyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    _lib.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)


_lib.glCreateProgram.argtypes = ()
_lib.glCreateProgram.restype = ctypes.c_uint
# GLuint = glCreateProgram()
def createProgram():
    return _lib.glCreateProgram()


_lib.glCreateShader.argtypes = ctypes.c_uint,
_lib.glCreateShader.restype = ctypes.c_uint
# GLuint = glCreateShader(GLenum type)
def createShader(type):
    return _lib.glCreateShader(type)


_lib.glCullFace.argtypes = ctypes.c_uint,
# void = glCullFace(GLenum mode)
def cullFace(mode):
    _lib.glCullFace(mode)


_lib.glDeleteBuffers.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glDeleteBuffers(GLsizei n, GLuint* buffers)
def deleteBuffer(buffer):
    n = 1
    buffers = (ctypes.c_uint*n)(buffer)
    res = _lib.glDeleteBuffers(n, buffers)


_lib.glDeleteFramebuffers.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glDeleteFramebuffers(GLsizei n, GLuint* framebuffers)
def deleteFramebuffer(framebuffer):
    n = 1
    buffers = (ctypes.c_uint*n)(framebuffer)
    res = _lib.glDeleteFramebuffers(n, framebuffers)


_lib.glDeleteProgram.argtypes = ctypes.c_uint,
# void = glDeleteProgram(GLuint program)
def deleteProgra(program):
    _lib.glDeleteProgram(program)


_lib.glDeleteRenderbuffers.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glDeleteRenderbuffers(GLsizei n, GLuint* renderbuffers)
def deleteRenderbuffer(renderbuffer):
    n = 1
    buffers = (ctypes.c_uint*n)(renderbuffer)
    res = _lib.glDeleteRenderbuffers(n, renderbuffers)


_lib.glDeleteShader.argtypes = ctypes.c_uint,
# void = glDeleteShader(GLuint shader)
def deleteShade(shader):
    _lib.glDeleteShader(shader)


_lib.glDeleteTextures.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glDeleteTextures(GLsizei n, GLuint* textures)
def deleteTexture(texture):
    n = 1
    buffers = (ctypes.c_uint*n)(texture)
    res = _lib.glDeleteTextures(n, textures)


_lib.glDepthFunc.argtypes = ctypes.c_uint,
# void = glDepthFunc(GLenum func)
def depthFunc(func):
    _lib.glDepthFunc(func)


_lib.glDepthMask.argtypes = ctypes.c_bool,
# void = glDepthMask(GLboolean flag)
def depthMask(flag):
    _lib.glDepthMask(flag)


_lib.glDepthRangef.argtypes = ctypes.c_float, ctypes.c_float,
# void = glDepthRangef(GLclampf zNear, GLclampf zFar)
def depthRangef(zNear, zFar):
    _lib.glDepthRangef(zNear, zFar)


_lib.glDetachShader.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glDetachShader(GLuint program, GLuint shader)
def detachShader(program, shader):
    _lib.glDetachShader(program, shader)


_lib.glDisable.argtypes = ctypes.c_uint,
# void = glDisable(GLenum cap)
def disable(cap):
    _lib.glDisable(cap)


_lib.glDisableVertexAttribArray.argtypes = ctypes.c_uint,
# void = glDisableVertexAttribArray(GLuint index)
def disableVertexAttribArray(index):
    _lib.glDisableVertexAttribArray(index)


_lib.glDrawArrays.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_int,
# void = glDrawArrays(GLenum mode, GLint first, GLsizei count)
def drawArrays(mode, first, count):
    _lib.glDrawArrays(mode, first, count)


_lib.glDrawElements.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_void_p,
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
    res = _lib.glDrawElements(mode, count, type, indices)


_lib.glEnable.argtypes = ctypes.c_uint,
# void = glEnable(GLenum cap)
def enable(cap):
    _lib.glEnable(cap)


_lib.glEnableVertexAttribArray.argtypes = ctypes.c_uint,
# void = glEnableVertexAttribArray(GLuint index)
def enableVertexAttribArray(index):
    _lib.glEnableVertexAttribArray(index)


_lib.glFinish.argtypes = ()
# void = glFinish()
def finish():
    _lib.glFinish()


_lib.glFlush.argtypes = ()
# void = glFlush()
def flush():
    _lib.glFlush()


_lib.glFramebufferRenderbuffer.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,
# void = glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
def framebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
    _lib.glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)


_lib.glFramebufferTexture2D.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_int,
# void = glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
def framebufferTexture2D(target, attachment, textarget, texture, level):
    _lib.glFramebufferTexture2D(target, attachment, textarget, texture, level)


_lib.glFrontFace.argtypes = ctypes.c_uint,
# void = glFrontFace(GLenum mode)
def frontFace(mode):
    _lib.glFrontFace(mode)


_lib.glGenBuffers.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glGenBuffers(GLsizei n, GLuint* buffers)
def createBuffer():
    n = 1
    buffers = (ctypes.c_uint*n)()
    res = _lib.glGenBuffers(n, buffers)
    return buffers[0]


_lib.glGenFramebuffers.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glGenFramebuffers(GLsizei n, GLuint* framebuffers)
def createFramebuffer():
    n = 1
    framebuffers = (ctypes.c_uint*n)()
    res = _lib.glGenFramebuffers(n, framebuffers)
    return framebuffers[0]


_lib.glGenRenderbuffers.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glGenRenderbuffers(GLsizei n, GLuint* renderbuffers)
def createRenderbuffer():
    n = 1
    renderbuffers = (ctypes.c_uint*n)()
    res = _lib.glGenRenderbuffers(n, renderbuffers)
    return renderbuffers[0]


_lib.glGenTextures.argtypes = ctypes.c_int, ctypes.POINTER(ctypes.c_uint),
# void = glGenTextures(GLsizei n, GLuint* textures)
def createTexture():
    n = 1
    textures = (ctypes.c_uint*n)()
    res = _lib.glGenTextures(n, textures)
    return textures[0]


_lib.glGenerateMipmap.argtypes = ctypes.c_uint,
# void = glGenerateMipmap(GLenum target)
def createerateMipma(target):
    _lib.glGenerateMipmap(target)


_lib.glGetActiveAttrib.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p,
# void = glGetActiveAttrib(GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name)
def getActiveAttrib(program, index):
    bufsize = 256
    length = (ctypes.c_int*1)()
    size = (ctypes.c_int*1)()
    type = (ctypes.c_uint*1)()
    name = ctypes.create_string_buffer(bufsize)
    res = _lib.glGetActiveAttrib(program, index, bufsize, length, size, type, name)
    name = name[:length[0]].decode('utf-8')
    return name, size[0], type[0]


_lib.glGetActiveUniform.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint), ctypes.c_char_p,
# void = glGetActiveUniform(GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name)
def getActiveUniform(program, index):
    bufsize = 256
    length = (ctypes.c_int*1)()
    size = (ctypes.c_int*1)()
    type = (ctypes.c_uint*1)()
    name = ctypes.create_string_buffer(bufsize)
    res = _lib.glGetActiveUniform(program, index, bufsize, length, size, type, name)
    name = name[:length[0]].decode('utf-8')
    return name, size[0], type[0]


_lib.glGetAttachedShaders.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint),
# void = glGetAttachedShaders(GLuint program, GLsizei maxcount, GLsizei* count, GLuint* shaders)
def getAttachedShaders(program):
    maxcount = 256
    count = (ctypes.c_int*1)()
    shaders = (ctypes.c_uint*1)()
    res = _lib.glGetAttachedShaders(program, maxcount, count, shaders)
    return tuple(shaders[:count[0]])


_lib.glGetAttribLocation.argtypes = ctypes.c_uint, ctypes.c_char_p,
_lib.glGetAttribLocation.restype = ctypes.c_int
# GLint = glGetAttribLocation(GLuint program, GLchar* name)
def getAttribLocation(program, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    res = _lib.glGetAttribLocation(program, name)
    return res


_lib.glGetBooleanv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_bool),
# void = glGetBooleanv(GLenum pname, GLboolean* params)
def getBooleanv(pname):
    data = (ctypes.c_bool*1)()
    res = _lib.glGetBooleanv(pname, params)
    return data[0]


_lib.glGetBufferParameteriv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
# void = glGetBufferParameteriv(GLenum target, GLenum pname, GLint* params)
def getBufferParameteriv(target, pname):
    data = (ctypes.c_int*1)()
    res = _lib.glGetBufferParameteriv(target, pname, params)
    return data[0]


_lib.glGetError.argtypes = ()
_lib.glGetError.restype = ctypes.c_uint
# GLenum = glGetError()
def getError():
    return _lib.glGetError()


_lib.glGetFloatv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
# void = glGetFloatv(GLenum pname, GLfloat* params)
def getFloatv(pname):
    data = (ctypes.c_float*1)()
    res = _lib.glGetFloatv(pname, params)
    return data[0]


_lib.glGetFramebufferAttachmentParameteriv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
# void = glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname, GLint* params)
def getFramebufferAttachmentParameteriv(target, attachment, pname):
    params = (ctypes.c_int*1)()
    res = _lib.glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)
    return params[0]


_lib.glGetIntegerv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
# void = glGetIntegerv(GLenum pname, GLint* params)
def getIntegerv(pname):
    data = (ctypes.c_int*1)()
    res = _lib.glGetIntegerv(pname, params)
    return data[0]


_lib.glGetProgramInfoLog.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p,
# void = glGetProgramInfoLog(GLuint program, GLsizei bufsize, GLsizei* length, GLchar* infolog)
def getProgramInfoLog(program):
    bufsize = 1024
    length = (ctypes.c_int*1)()
    infolog = ctypes.create_string_buffer(bufsize)
    res = _lib.glGetProgramInfoLog(program, bufsize, length, infolog)
    return infolog[:length[0]].decode('utf-8')


_lib.glGetProgramiv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
# void = glGetProgramiv(GLuint program, GLenum pname, GLint* params)
def getProgramiv(program, pname):
    params = (ctypes.c_int*1)()
    res = _lib.glGetProgramiv(program, pname, params)
    return params[0]


_lib.glGetRenderbufferParameteriv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
# void = glGetRenderbufferParameteriv(GLenum target, GLenum pname, GLint* params)
def getRenderbufferParameteriv(target, pname):
    params = (ctypes.c_int*1)()
    res = _lib.glGetRenderbufferParameteriv(target, pname, params)
    return params[0]


_lib.glGetShaderInfoLog.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p,
# void = glGetShaderInfoLog(GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* infolog)
def getShaderInfoLog(shader):
    bufsize = 1024
    length = (ctypes.c_int*1)()
    infolog = ctypes.create_string_buffer(bufsize)
    res = _lib.glGetShaderInfoLog(shader, bufsize, length, infolog)
    return infolog[:length[0]].decode('utf-8')


_lib.glGetShaderPrecisionFormat.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
# void = glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint* range, GLint* precision)
def getShaderPrecisionFormat(shadertype, precisiontype):
    range = (ctypes.c_int*1)()
    precision = (ctypes.c_int*1)()
    res = _lib.glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)
    return range[0], precision[0]


_lib.glGetShaderSource.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_char_p,
# void = glGetShaderSource(GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* source)
def getShaderSource(shader):
    bufSize = 1024*1024
    length = (ctypes.c_int*1)()
    source = (ctypes.c_char*bufsize)()
    res = _lib.glGetShaderSource(shader, bufsize, length, source)
    return source.value[:length[0]].decode('utf-8')


_lib.glGetShaderiv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
# void = glGetShaderiv(GLuint shader, GLenum pname, GLint* params)
def getShaderiv(shader, pname):
    params = (ctypes.c_int*1)()
    res = _lib.glGetShaderiv(shader, pname, params)
    return params[0]


_lib.glGetString.argtypes = ctypes.c_uint,
_lib.glGetString.restype = ctypes.c_char_p
# GLubyte* = glGetString(GLenum name)
def getString(pname):
    res = _lib.glGetString(name)
    return res.value


_lib.glGetTexParameterfv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
_lib.glGetTexParameteriv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
def getTexParameterfv(target, pname):
    params = (ctypes.c_float*1)()
    _lib.glGetTexParameterfv(target, pname, params)
    return params[0]
def getTexParameteriv(target, pname):
    params = (ctypes.c_int*1)()
    _lib.glGetTexParameteriv(target, pname, params)
    return params[0]


_lib.glGetUniformfv.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
_lib.glGetUniformiv.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int),
def getUniformfv(program, location):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_float*16)(*[d for i in range(16)])
    _lib.glGetUniformfv(program, location, values)
    return tuple([val for val in values if val!=d])
def getUniformiv(program, location):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_int*16)(*[d for i in range(16)])
    _lib.glGetUniformiv(program, location, values)
    return tuple([val for val in values if val!=d])


_lib.glGetUniformLocation.argtypes = ctypes.c_uint, ctypes.c_char_p,
_lib.glGetUniformLocation.restype = ctypes.c_int
# GLint = glGetUniformLocation(GLuint program, GLchar* name)
def getUniformLocation(program, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    res = _lib.glGetUniformLocation(program, name)
    return res


_lib.glGetVertexAttribfv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
_lib.glGetVertexAttribiv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
def getVertexAttrfv(index, pname):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_float*4)(*[d for i in range(4)])
    _lib.glGetVertexAttrfv(index, pname, values)
    return tuple([val for val in values if val!=d])
def getVertexAttriv(index, pname):
    d = -99999  # Note: this is a bit dangerous
    values = (ctypes.c_int*4)(*[d for i in range(4)])
    _lib.glGetVertexAttriv(index, pname, values)
    return tuple([val for val in values if val!=d])


_lib.glGetVertexAttribPointerv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_void_p),
# void = glGetVertexAttribPointerv(GLuint index, GLenum pname, GLvoid** pointer)
def getVertexAttribPointerv(index, pname):
    pointer = (ctypes.c_void_p*1)()
    res = _lib.glGetVertexAttribPointerv(index, pname, pointer)
    return pointer[0]


_lib.glHint.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glHint(GLenum target, GLenum mode)
def hint(target, mode):
    _lib.glHint(target, mode)


_lib.glIsBuffer.argtypes = ctypes.c_uint,
_lib.glIsBuffer.restype = ctypes.c_bool
# GLboolean = glIsBuffer(GLuint buffer)
def isBuffer(buffer):
    return _lib.glIsBuffer(buffer)


_lib.glIsEnabled.argtypes = ctypes.c_uint,
_lib.glIsEnabled.restype = ctypes.c_bool
# GLboolean = glIsEnabled(GLenum cap)
def isEnabled(cap):
    return _lib.glIsEnabled(cap)


_lib.glIsFramebuffer.argtypes = ctypes.c_uint,
_lib.glIsFramebuffer.restype = ctypes.c_bool
# GLboolean = glIsFramebuffer(GLuint framebuffer)
def isFramebuffer(framebuffer):
    return _lib.glIsFramebuffer(framebuffer)


_lib.glIsProgram.argtypes = ctypes.c_uint,
_lib.glIsProgram.restype = ctypes.c_bool
# GLboolean = glIsProgram(GLuint program)
def isProgram(program):
    return _lib.glIsProgram(program)


_lib.glIsRenderbuffer.argtypes = ctypes.c_uint,
_lib.glIsRenderbuffer.restype = ctypes.c_bool
# GLboolean = glIsRenderbuffer(GLuint renderbuffer)
def isRenderbuffer(renderbuffer):
    return _lib.glIsRenderbuffer(renderbuffer)


_lib.glIsShader.argtypes = ctypes.c_uint,
_lib.glIsShader.restype = ctypes.c_bool
# GLboolean = glIsShader(GLuint shader)
def isShader(shader):
    return _lib.glIsShader(shader)


_lib.glIsTexture.argtypes = ctypes.c_uint,
_lib.glIsTexture.restype = ctypes.c_bool
# GLboolean = glIsTexture(GLuint texture)
def isTexture(texture):
    return _lib.glIsTexture(texture)


_lib.glLineWidth.argtypes = ctypes.c_float,
# void = glLineWidth(GLfloat width)
def lineWidth(width):
    _lib.glLineWidth(width)


_lib.glLinkProgram.argtypes = ctypes.c_uint,
# void = glLinkProgram(GLuint program)
def linkProgram(program):
    _lib.glLinkProgram(program)


_lib.glPixelStorei.argtypes = ctypes.c_uint, ctypes.c_int,
# void = glPixelStorei(GLenum pname, GLint param)
def pixelStorei(pname, param):
    _lib.glPixelStorei(pname, param)


_lib.glPolygonOffset.argtypes = ctypes.c_float, ctypes.c_float,
# void = glPolygonOffset(GLfloat factor, GLfloat units)
def polygonOffset(factor, units):
    _lib.glPolygonOffset(factor, units)


_lib.glReadPixels.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,
# void = glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels)
def readPixels(x, y, width, height, format, type):
    """ Return pixels as bytes.
    """
    size = width*height
    pixels = (ctypes.c_uint8*size)()
    res = _lib.glReadPixels(x, y, width, height, format, type, pixels)
    return bytes(pixels)


_lib.glRenderbufferStorage.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_int,
# void = glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height)
def renderbufferStorage(target, internalformat, width, height):
    _lib.glRenderbufferStorage(target, internalformat, width, height)


_lib.glSampleCoverage.argtypes = ctypes.c_float, ctypes.c_bool,
# void = glSampleCoverage(GLclampf value, GLboolean invert)
def sampleCoverage(value, invert):
    _lib.glSampleCoverage(value, invert)


_lib.glScissor.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
# void = glScissor(GLint x, GLint y, GLsizei width, GLsizei height)
def scissor(x, y, width, height):
    _lib.glScissor(x, y, width, height)


_lib.glShaderSource.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int),
# void = glShaderSource(GLuint shader, GLsizei count, GLchar** string, GLint* length)
def shaderSource(shader, *strings):
    if len(strings) == 1 and isinstance(strings[0], (tuple, list)):
        strings = strings[0]
    count = len(strings)
    string = (ctypes.c_char_p*count)(*[s.encode('utf-8') for s in strings])
    length = (ctypes.c_int*count)(*[len(s) for s in strings])
    res = _lib.glShaderSource(shader, count, string, length)


_lib.glStencilFunc.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_uint,
# void = glStencilFunc(GLenum func, GLint ref, GLuint mask)
def stencilFunc(func, ref, mask):
    _lib.glStencilFunc(func, ref, mask)


_lib.glStencilFuncSeparate.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_uint,
# void = glStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask)
def stencilFuncSeparate(face, func, ref, mask):
    _lib.glStencilFuncSeparate(face, func, ref, mask)


_lib.glStencilMask.argtypes = ctypes.c_uint,
# void = glStencilMask(GLuint mask)
def stencilMask(mask):
    _lib.glStencilMask(mask)


_lib.glStencilMaskSeparate.argtypes = ctypes.c_uint, ctypes.c_uint,
# void = glStencilMaskSeparate(GLenum face, GLuint mask)
def stencilMaskSeparate(face, mask):
    _lib.glStencilMaskSeparate(face, mask)


_lib.glStencilOp.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,
# void = glStencilOp(GLenum fail, GLenum zfail, GLenum zpass)
def stencilOp(fail, zfail, zpass):
    _lib.glStencilOp(fail, zfail, zpass)


_lib.glStencilOpSeparate.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,
# void = glStencilOpSeparate(GLenum face, GLenum fail, GLenum zfail, GLenum zpass)
def stencilOpSeparate(face, fail, zfail, zpass):
    _lib.glStencilOpSeparate(face, fail, zfail, zpass)


_lib.glTexImage2D.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,
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
    res = _lib.glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)


_lib.glTexParameterf.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_float,
_lib.glTexParameterfv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
_lib.glTexParameteri.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.c_int,
_lib.glTexParameteriv.argtypes = ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
def texParameterf(target, pname, param):
    _lib.glTexParameterf(target, pname, param)
def texParameteri(target, pname, param):
    _lib.glTexParameteri(target, pname, param)


_lib.glTexSubImage2D.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,
# void = glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels)
def texSubImage2D(target, level, xoffset, yoffset, format, type, pixels):
    if not pixels.flags['C_CONTIGUOUS']:
        pixels = pixels.copy('C')
    pixels_ = pixels
    pixels = pixels_.ctypes.data
    width, height = pixels_.shape[:2]
    res = _lib.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)


_lib.glUniform1f.argtypes = ctypes.c_int, ctypes.c_float,
_lib.glUniform1fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
_lib.glUniform1i.argtypes = ctypes.c_int, ctypes.c_int,
_lib.glUniform1iv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),
_lib.glUniform2f.argtypes = ctypes.c_int, ctypes.c_float, ctypes.c_float,
_lib.glUniform2fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
_lib.glUniform2i.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int,
_lib.glUniform2iv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),
_lib.glUniform3f.argtypes = ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float,
_lib.glUniform3fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
_lib.glUniform3i.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
_lib.glUniform3iv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),
_lib.glUniform4f.argtypes = ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
_lib.glUniform4fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float),
_lib.glUniform4i.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
_lib.glUniform4iv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int),
def uniform1f(location, v1):
    _lib.glUniform1f(location, v1)
def uniform2f(location, v1, v2):
    _lib.glUniform2f(location, v1, v2)
def uniform3f(location, v1, v2, v3):
    _lib.glUniform3f(location, v1, v2, v3)
def uniform4f(location, v1, v2, v3, v4):
    _lib.glUniform4f(location, v1, v2, v3, v4)
def uniform1i(location, v1):
    _lib.glUniform1i(location, v1)
def uniform2i(location, v1, v2):
    _lib.glUniform2i(location, v1, v2)
def uniform3i(location, v1, v2, v3):
    _lib.glUniform3i(location, v1, v2, v3)
def uniform4i(location, v1, v2, v3, v4):
    _lib.glUniform4i(location, v1, v2, v3, v4)
def uniform1fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniform1fv(location, count, values)
def uniform2fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniform2fv(location, count, values)
def uniform3fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniform3fv(location, count, values)
def uniform4fv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniform4fv(location, count, values)
def uniform1iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    _lib.glUniform1iv(location, count, values)
def uniform2iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    _lib.glUniform2iv(location, count, values)
def uniform3iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    _lib.glUniform3iv(location, count, values)
def uniform4iv(location, count, values):
    values = [val for val in values]
    values = (ctypes.c_int*len(values))(*values)
    _lib.glUniform4iv(location, count, values)


_lib.glUniformMatrix2fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_float),
_lib.glUniformMatrix3fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_float),
_lib.glUniformMatrix4fv.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_float),
def uniformMatrix2fv(location, count, transpose, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniformMatrix2fv(location, count, transpose, values)
def uniformMatrix3fv(location, count, transpose, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniformMatrix3fv(location, count, transpose, values)
def uniformMatrix4fv(location, count, transpose, values):
    values = [val for val in values]
    values = (ctypes.c_float*len(values))(*values)
    _lib.glUniformMatrix4fv(location, count, transpose, values)


_lib.glUseProgram.argtypes = ctypes.c_uint,
# void = glUseProgram(GLuint program)
def useProgram(program):
    _lib.glUseProgram(program)


_lib.glValidateProgram.argtypes = ctypes.c_uint,
# void = glValidateProgram(GLuint program)
def validateProgram(program):
    _lib.glValidateProgram(program)


_lib.glVertexAttrib1f.argtypes = ctypes.c_uint, ctypes.c_float,
_lib.glVertexAttrib1fv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
_lib.glVertexAttrib2f.argtypes = ctypes.c_uint, ctypes.c_float, ctypes.c_float,
_lib.glVertexAttrib2fv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
_lib.glVertexAttrib3f.argtypes = ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float,
_lib.glVertexAttrib3fv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
_lib.glVertexAttrib4f.argtypes = ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
_lib.glVertexAttrib4fv.argtypes = ctypes.c_uint, ctypes.POINTER(ctypes.c_float),
def vertexAttrib1f(index, v1):
    _lib.glVertexAttrib1f(index, v1)
def vertexAttrib2f(index, v1, v2):
    _lib.glVertexAttrib2f(index, v1, v2)
def vertexAttrib3f(index, v1, v2, v3):
    _lib.glVertexAttrib3f(index, v1, v2, v3)
def vertexAttrib4f(index, v1, v2, v3, v4):
    _lib.glVertexAttrib4f(index, v1, v2, v3, v4)


_lib.glVertexAttribPointer.argtypes = ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_bool, ctypes.c_int, ctypes.c_void_p,
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
    res = _lib.glVertexAttribPointer(indx, size, type, normalized, stride, ptr)


_lib.glViewport.argtypes = ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
# void = glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
def viewport(x, y, width, height):
    _lib.glViewport(x, y, width, height)


