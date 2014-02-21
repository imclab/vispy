"""

THIS CODE IS AUTO-GENERATED. DO NOT EDIT.

GL API X

"""

from .import _main
PROXY = _main.__dict__

def glActiveTexture(texture):
    return PROXY["activeTexture"](texture)


def glAttachShader(program, shader):
    return PROXY["attachShader"](program, shader)


def glBindAttribLocation(program, index, name):
    return PROXY["bindAttribLocation"](program, index, name)


def glBindBuffer(target, buffer):
    return PROXY["bindBuffer"](target, buffer)


def glBindFramebuffer(target, framebuffer):
    return PROXY["bindFramebuffer"](target, framebuffer)


def glBindRenderbuffer(target, renderbuffer):
    return PROXY["bindRenderbuffer"](target, renderbuffer)


def glBindTexture(target, texture):
    return PROXY["bindTexture"](target, texture)


def glBlendColor(red, green, blue, alpha):
    return PROXY["blendColor"](red, green, blue, alpha)


def glBlendEquation(mode):
    return PROXY["blendEquation"](mode)


def glBlendEquationSeparate(modeRGB, modeAlpha):
    return PROXY["blendEquationSeparate"](modeRGB, modeAlpha)


def glBlendFunc(sfactor, dfactor):
    return PROXY["blendFunc"](sfactor, dfactor)


def glBlendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha):
    return PROXY["blendFuncSeparate"](srcRGB, dstRGB, srcAlpha, dstAlpha)


def glBufferData(target, data, usage):
    return PROXY["bufferData"](target, data, usage)


def glBufferSubData(target, offset, data):
    return PROXY["bufferSubData"](target, offset, data)


def glCheckFramebufferStatus(target):
    return PROXY["checkFramebufferStatus"](target)


def glClear(mask):
    return PROXY["clear"](mask)


def glClearColor(red, green, blue, alpha):
    return PROXY["clearColor"](red, green, blue, alpha)


def glClearDepthf(depth):
    return PROXY["clearDepthf"](depth)


def glClearStencil(s):
    return PROXY["clearStencil"](s)


def glColorMask(red, green, blue, alpha):
    return PROXY["colorMask"](red, green, blue, alpha)


def glCompileShader(shader):
    return PROXY["compileShader"](shader)


def glCompressedTexImage2D(target, level, internalformat, width=0, height=0, border=0, data=None):
    return PROXY["compressedTexImage2D"](target, level, internalformat, width=0, height=0, border=0, data=None)


def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data):
    return PROXY["compressedTexSubImage2D"](target, level, xoffset, yoffset, width, height, format, data)


def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
    return PROXY["copyTexImage2D"](target, level, internalformat, x, y, width, height, border)


def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    return PROXY["copyTexSubImage2D"](target, level, xoffset, yoffset, x, y, width, height)


def glCreateProgram():
    return PROXY["createProgram"]()


def glCreateShader(type):
    return PROXY["createShader"](type)


def glCullFace(mode):
    return PROXY["cullFace"](mode)


def glDeleteBuffer(buffer):
    return PROXY["deleteBuffer"](buffer)


def glDeleteFramebuffer(framebuffer):
    return PROXY["deleteFramebuffer"](framebuffer)


def glDeleteProgra(program):
    return PROXY["deleteProgra"](program)


def glDeleteRenderbuffer(renderbuffer):
    return PROXY["deleteRenderbuffer"](renderbuffer)


def glDeleteShade(shader):
    return PROXY["deleteShade"](shader)


def glDeleteTexture(texture):
    return PROXY["deleteTexture"](texture)


def glDepthFunc(func):
    return PROXY["depthFunc"](func)


def glDepthMask(flag):
    return PROXY["depthMask"](flag)


def glDepthRangef(zNear, zFar):
    return PROXY["depthRangef"](zNear, zFar)


def glDetachShader(program, shader):
    return PROXY["detachShader"](program, shader)


def glDisable(cap):
    return PROXY["disable"](cap)


def glDisableVertexAttribArray(index):
    return PROXY["disableVertexAttribArray"](index)


def glDrawArrays(mode, first, count):
    return PROXY["drawArrays"](mode, first, count)


def glDrawElements(mode, count, type, offset):
    return PROXY["drawElements"](mode, count, type, offset)


def glEnable(cap):
    return PROXY["enable"](cap)


def glEnableVertexAttribArray(index):
    return PROXY["enableVertexAttribArray"](index)


def glFinish():
    return PROXY["finish"]()


def glFlush():
    return PROXY["flush"]()


def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
    return PROXY["framebufferRenderbuffer"](target, attachment, renderbuffertarget, renderbuffer)


def glFramebufferTexture2D(target, attachment, textarget, texture, level):
    return PROXY["framebufferTexture2D"](target, attachment, textarget, texture, level)


def glFrontFace(mode):
    return PROXY["frontFace"](mode)


def glCreateBuffer():
    return PROXY["createBuffer"]()


def glCreateFramebuffer():
    return PROXY["createFramebuffer"]()


def glCreateRenderbuffer():
    return PROXY["createRenderbuffer"]()


def glCreateTexture():
    return PROXY["createTexture"]()


def glCreateerateMipma(target):
    return PROXY["createerateMipma"](target)


def glGetActiveAttrib(program, index):
    return PROXY["getActiveAttrib"](program, index)


def glGetActiveUniform(program, index):
    return PROXY["getActiveUniform"](program, index)


def glGetAttachedShaders(program):
    return PROXY["getAttachedShaders"](program)


def glGetAttribLocation(program, name):
    return PROXY["getAttribLocation"](program, name)


def glGetBooleanv(pname):
    return PROXY["getBooleanv"](pname)


def glGetBufferParameteriv(target, pname):
    return PROXY["getBufferParameteriv"](target, pname)


def glGetError():
    return PROXY["getError"]()


def glGetFloatv(pname):
    return PROXY["getFloatv"](pname)


def glGetFramebufferAttachmentParameteriv(target, attachment, pname):
    return PROXY["getFramebufferAttachmentParameteriv"](target, attachment, pname)


def glGetIntegerv(pname):
    return PROXY["getIntegerv"](pname)


def glGetProgramInfoLog(program):
    return PROXY["getProgramInfoLog"](program)


def glGetProgramiv(program, pname):
    return PROXY["getProgramiv"](program, pname)


def glGetRenderbufferParameteriv(target, pname):
    return PROXY["getRenderbufferParameteriv"](target, pname)


def glGetShaderInfoLog(shader):
    return PROXY["getShaderInfoLog"](shader)


def glGetShaderPrecisionFormat(shadertype, precisiontype):
    return PROXY["getShaderPrecisionFormat"](shadertype, precisiontype)


def glGetShaderSource(shader):
    return PROXY["getShaderSource"](shader)


def glGetShaderiv(shader, pname):
    return PROXY["getShaderiv"](shader, pname)


def glGetString(pname):
    return PROXY["getString"](pname)


def glGetTexParameterfv(target, pname):
    return PROXY["getTexParameterfv"](target, pname)
def glGetTexParameteriv(target, pname):
    return PROXY["getTexParameteriv"](target, pname)


def glGetUniformfv(program, location):
    return PROXY["getUniformfv"](program, location)
def glGetUniformiv(program, location):
    return PROXY["getUniformiv"](program, location)


def glGetUniformLocation(program, name):
    return PROXY["getUniformLocation"](program, name)


def glGetVertexAttribfv(index, pname):
    return PROXY["getVertexAttribfv"](index, pname)
def glGetVertexAttribiv(index, pname):
    return PROXY["getVertexAttribiv"](index, pname)


def glGetVertexAttribPointerv(index, pname):
    return PROXY["getVertexAttribPointerv"](index, pname)


def glHint(target, mode):
    return PROXY["hint"](target, mode)


def glIsBuffer(buffer):
    return PROXY["isBuffer"](buffer)


def glIsEnabled(cap):
    return PROXY["isEnabled"](cap)


def glIsFramebuffer(framebuffer):
    return PROXY["isFramebuffer"](framebuffer)


def glIsProgram(program):
    return PROXY["isProgram"](program)


def glIsRenderbuffer(renderbuffer):
    return PROXY["isRenderbuffer"](renderbuffer)


def glIsShader(shader):
    return PROXY["isShader"](shader)


def glIsTexture(texture):
    return PROXY["isTexture"](texture)


def glLineWidth(width):
    return PROXY["lineWidth"](width)


def glLinkProgram(program):
    return PROXY["linkProgram"](program)


def glPixelStorei(pname, param):
    return PROXY["pixelStorei"](pname, param)


def glPolygonOffset(factor, units):
    return PROXY["polygonOffset"](factor, units)


def glReadPixels(x, y, width, height, format, type):
    return PROXY["readPixels"](x, y, width, height, format, type)


def glRenderbufferStorage(target, internalformat, width, height):
    return PROXY["renderbufferStorage"](target, internalformat, width, height)


def glSampleCoverage(value, invert):
    return PROXY["sampleCoverage"](value, invert)


def glScissor(x, y, width, height):
    return PROXY["scissor"](x, y, width, height)


def glShaderSource(shader, *strings):
    return PROXY["shaderSource"](shader, *strings)


def glStencilFunc(func, ref, mask):
    return PROXY["stencilFunc"](func, ref, mask)


def glStencilFuncSeparate(face, func, ref, mask):
    return PROXY["stencilFuncSeparate"](face, func, ref, mask)


def glStencilMask(mask):
    return PROXY["stencilMask"](mask)


def glStencilMaskSeparate(face, mask):
    return PROXY["stencilMaskSeparate"](face, mask)


def glStencilOp(fail, zfail, zpass):
    return PROXY["stencilOp"](fail, zfail, zpass)


def glStencilOpSeparate(face, fail, zfail, zpass):
    return PROXY["stencilOpSeparate"](face, fail, zfail, zpass)


def glTexImage2D(target, level, internalformat, format, type, pixels):
    return PROXY["texImage2D"](target, level, internalformat, format, type, pixels)


def glTexParameterf(target, pname, param):
    return PROXY["texParameterf"](target, pname, param)
def glTexParameteri(target, pname, param):
    return PROXY["texParameteri"](target, pname, param)


def glTexSubImage2D(target, level, xoffset, yoffset, format, type, pixels):
    return PROXY["texSubImage2D"](target, level, xoffset, yoffset, format, type, pixels)


def glUniform1f(location, v1):
    return PROXY["uniform1f"](location, v1)
def glUniform2f(location, v1, v2):
    return PROXY["uniform2f"](location, v1, v2)
def glUniform3f(location, v1, v2, v3):
    return PROXY["uniform3f"](location, v1, v2, v3)
def glUniform4f(location, v1, v2, v3, v4):
    return PROXY["uniform4f"](location, v1, v2, v3, v4)
def glUniform1i(location, v1):
    return PROXY["uniform1i"](location, v1)
def glUniform2i(location, v1, v2):
    return PROXY["uniform2i"](location, v1, v2)
def glUniform3i(location, v1, v2, v3):
    return PROXY["uniform3i"](location, v1, v2, v3)
def glUniform4i(location, v1, v2, v3, v4):
    return PROXY["uniform4i"](location, v1, v2, v3, v4)
def glUniform1fv(location, count, values):
    return PROXY["uniform1fv"](location, count, values)
def glUniform2fv(location, count, values):
    return PROXY["uniform2fv"](location, count, values)
def glUniform3fv(location, count, values):
    return PROXY["uniform3fv"](location, count, values)
def glUniform4fv(location, count, values):
    return PROXY["uniform4fv"](location, count, values)
def glUniform1iv(location, count, values):
    return PROXY["uniform1iv"](location, count, values)
def glUniform2iv(location, count, values):
    return PROXY["uniform2iv"](location, count, values)
def glUniform3iv(location, count, values):
    return PROXY["uniform3iv"](location, count, values)
def glUniform4iv(location, count, values):
    return PROXY["uniform4iv"](location, count, values)


def glUniformMatrix2fv(location, count, transpose, values):
    return PROXY["uniformMatrix2fv"](location, count, transpose, values)
def glUniformMatrix3fv(location, count, transpose, values):
    return PROXY["uniformMatrix3fv"](location, count, transpose, values)
def glUniformMatrix4fv(location, count, transpose, values):
    return PROXY["uniformMatrix4fv"](location, count, transpose, values)


def glUseProgram(program):
    return PROXY["useProgram"](program)


def glValidateProgram(program):
    return PROXY["validateProgram"](program)


def glVertexAttrib1f(index, v1):
    return PROXY["vertexAttrib1f"](index, v1)
def glVertexAttrib2f(index, v1, v2):
    return PROXY["vertexAttrib2f"](index, v1, v2)
def glVertexAttrib3f(index, v1, v2, v3):
    return PROXY["vertexAttrib3f"](index, v1, v2, v3)
def glVertexAttrib4f(index, v1, v2, v3, v4):
    return PROXY["vertexAttrib4f"](index, v1, v2, v3, v4)


def glVertexAttribPointer(indx, size, type, normalized, stride, offset):
    return PROXY["vertexAttribPointer"](indx, size, type, normalized, stride, offset)


def glViewport(x, y, width, height):
    return PROXY["viewport"](x, y, width, height)


