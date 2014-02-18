"""

THIS CODE IS AUTO-GENERATED. DO NOT EDIT.

GL API X

"""
def activeTexture(texture):
    return PROXY["activeTexture"](texture)


def attachShader(program, shader):
    return PROXY["attachShader"](program, shader)


def bindAttribLocation(program, index, name):
    return PROXY["bindAttribLocation"](program, index, name)


def bindBuffer(target, buffer):
    return PROXY["bindBuffer"](target, buffer)


def bindFramebuffer(target, framebuffer):
    return PROXY["bindFramebuffer"](target, framebuffer)


def bindRenderbuffer(target, renderbuffer):
    return PROXY["bindRenderbuffer"](target, renderbuffer)


def bindTexture(target, texture):
    return PROXY["bindTexture"](target, texture)


def blendColor(red, green, blue, alpha):
    return PROXY["blendColor"](red, green, blue, alpha)


def blendEquation(mode):
    return PROXY["blendEquation"](mode)


def blendEquationSeparate(modeRGB, modeAlpha):
    return PROXY["blendEquationSeparate"](modeRGB, modeAlpha)


def blendFunc(sfactor, dfactor):
    return PROXY["blendFunc"](sfactor, dfactor)


def blendFuncSeparate(srcRGB, dstRGB, srcAlpha, dstAlpha):
    return PROXY["blendFuncSeparate"](srcRGB, dstRGB, srcAlpha, dstAlpha)


def bufferData(target, data, usage):
    return PROXY["bufferData"](target, data, usage)


def bufferSubData(target, offset, data):
    return PROXY["bufferSubData"](target, offset, data)


def checkFramebufferStatus(target):
    return PROXY["checkFramebufferStatus"](target)


def clear(mask):
    return PROXY["clear"](mask)


def clearColor(red, green, blue, alpha):
    return PROXY["clearColor"](red, green, blue, alpha)


def clearDepthf(depth):
    return PROXY["clearDepthf"](depth)


def clearStencil(s):
    return PROXY["clearStencil"](s)


def colorMask(red, green, blue, alpha):
    return PROXY["colorMask"](red, green, blue, alpha)


def compileShader(shader):
    return PROXY["compileShader"](shader)


def compressedTexImage2D(target, level, internalformat, width=0, height=0, border=0, data=None):
    return PROXY["compressedTexImage2D"](target, level, internalformat, width=0, height=0, border=0, data=None)


def compressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data):
    return PROXY["compressedTexSubImage2D"](target, level, xoffset, yoffset, width, height, format, data)


def copyTexImage2D(target, level, internalformat, x, y, width, height, border):
    return PROXY["copyTexImage2D"](target, level, internalformat, x, y, width, height, border)


def copyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    return PROXY["copyTexSubImage2D"](target, level, xoffset, yoffset, x, y, width, height)


def createProgram():
    return PROXY["createProgram"]()


def createShader(type):
    return PROXY["createShader"](type)


def cullFace(mode):
    return PROXY["cullFace"](mode)


def deleteBuffer(buffer):
    return PROXY["deleteBuffer"](buffer)


def deleteFramebuffer(framebuffer):
    return PROXY["deleteFramebuffer"](framebuffer)


def deleteProgra(program):
    return PROXY["deleteProgra"](program)


def deleteRenderbuffer(renderbuffer):
    return PROXY["deleteRenderbuffer"](renderbuffer)


def deleteShade(shader):
    return PROXY["deleteShade"](shader)


def deleteTexture(texture):
    return PROXY["deleteTexture"](texture)


def depthFunc(func):
    return PROXY["depthFunc"](func)


def depthMask(flag):
    return PROXY["depthMask"](flag)


def depthRangef(zNear, zFar):
    return PROXY["depthRangef"](zNear, zFar)


def detachShader(program, shader):
    return PROXY["detachShader"](program, shader)


def disable(cap):
    return PROXY["disable"](cap)


def disableVertexAttribArray(index):
    return PROXY["disableVertexAttribArray"](index)


def drawArrays(mode, first, count):
    return PROXY["drawArrays"](mode, first, count)


def drawElements(mode, count, type, offset):
    return PROXY["drawElements"](mode, count, type, offset)


def enable(cap):
    return PROXY["enable"](cap)


def enableVertexAttribArray(index):
    return PROXY["enableVertexAttribArray"](index)


def finish():
    return PROXY["finish"]()


def flush():
    return PROXY["flush"]()


def framebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
    return PROXY["framebufferRenderbuffer"](target, attachment, renderbuffertarget, renderbuffer)


def framebufferTexture2D(target, attachment, textarget, texture, level):
    return PROXY["framebufferTexture2D"](target, attachment, textarget, texture, level)


def frontFace(mode):
    return PROXY["frontFace"](mode)


def createBuffer():
    return PROXY["createBuffer"]()


def createFramebuffer():
    return PROXY["createFramebuffer"]()


def createRenderbuffer():
    return PROXY["createRenderbuffer"]()


def createTexture():
    return PROXY["createTexture"]()


def createerateMipma(target):
    return PROXY["createerateMipma"](target)


def getActiveAttrib(program, index):
    return PROXY["getActiveAttrib"](program, index)


def getActiveUniform(program, index):
    return PROXY["getActiveUniform"](program, index)


def getAttachedShaders(program):
    return PROXY["getAttachedShaders"](program)


def getAttribLocation(program, name):
    return PROXY["getAttribLocation"](program, name)


def getBooleanv(pname):
    return PROXY["getBooleanv"](pname)


def getBufferParameteriv(target, pname):
    return PROXY["getBufferParameteriv"](target, pname)


def getError():
    return PROXY["getError"]()


def getFloatv(pname):
    return PROXY["getFloatv"](pname)


def getFramebufferAttachmentParameteriv(target, attachment, pname):
    return PROXY["getFramebufferAttachmentParameteriv"](target, attachment, pname)


def getIntegerv(pname):
    return PROXY["getIntegerv"](pname)


def getProgramInfoLog(program):
    return PROXY["getProgramInfoLog"](program)


def getProgramiv(program, pname):
    return PROXY["getProgramiv"](program, pname)


def getRenderbufferParameteriv(target, pname):
    return PROXY["getRenderbufferParameteriv"](target, pname)


def getShaderInfoLog(shader):
    return PROXY["getShaderInfoLog"](shader)


def getShaderPrecisionFormat(shadertype, precisiontype):
    return PROXY["getShaderPrecisionFormat"](shadertype, precisiontype)


def getShaderSource(shader):
    return PROXY["getShaderSource"](shader)


def getShaderiv(shader, pname):
    return PROXY["getShaderiv"](shader, pname)


def getString(pname):
    return PROXY["getString"](pname)


def getTexParameterfv(target, pname):
    return PROXY["getTexParameterfv"](target, pname)
def getTexParameteriv(target, pname):
    return PROXY["getTexParameteriv"](target, pname)


def getUniformfv(program, location):
    return PROXY["getUniformfv"](program, location)
def getUniformiv(program, location):
    return PROXY["getUniformiv"](program, location)


def getUniformLocation(program, name):
    return PROXY["getUniformLocation"](program, name)


def getVertexAttrfv(index, pname):
    return PROXY["getVertexAttrfv"](index, pname)
def getVertexAttriv(index, pname):
    return PROXY["getVertexAttriv"](index, pname)


def getVertexAttribPointerv(index, pname):
    return PROXY["getVertexAttribPointerv"](index, pname)


def hint(target, mode):
    return PROXY["hint"](target, mode)


def isBuffer(buffer):
    return PROXY["isBuffer"](buffer)


def isEnabled(cap):
    return PROXY["isEnabled"](cap)


def isFramebuffer(framebuffer):
    return PROXY["isFramebuffer"](framebuffer)


def isProgram(program):
    return PROXY["isProgram"](program)


def isRenderbuffer(renderbuffer):
    return PROXY["isRenderbuffer"](renderbuffer)


def isShader(shader):
    return PROXY["isShader"](shader)


def isTexture(texture):
    return PROXY["isTexture"](texture)


def lineWidth(width):
    return PROXY["lineWidth"](width)


def linkProgram(program):
    return PROXY["linkProgram"](program)


def pixelStorei(pname, param):
    return PROXY["pixelStorei"](pname, param)


def polygonOffset(factor, units):
    return PROXY["polygonOffset"](factor, units)


def readPixels(x, y, width, height, format, type):
    return PROXY["readPixels"](x, y, width, height, format, type)


def renderbufferStorage(target, internalformat, width, height):
    return PROXY["renderbufferStorage"](target, internalformat, width, height)


def sampleCoverage(value, invert):
    return PROXY["sampleCoverage"](value, invert)


def scissor(x, y, width, height):
    return PROXY["scissor"](x, y, width, height)


def shaderSource(shader, *strings):
    return PROXY["shaderSource"](shader, *strings)


def stencilFunc(func, ref, mask):
    return PROXY["stencilFunc"](func, ref, mask)


def stencilFuncSeparate(face, func, ref, mask):
    return PROXY["stencilFuncSeparate"](face, func, ref, mask)


def stencilMask(mask):
    return PROXY["stencilMask"](mask)


def stencilMaskSeparate(face, mask):
    return PROXY["stencilMaskSeparate"](face, mask)


def stencilOp(fail, zfail, zpass):
    return PROXY["stencilOp"](fail, zfail, zpass)


def stencilOpSeparate(face, fail, zfail, zpass):
    return PROXY["stencilOpSeparate"](face, fail, zfail, zpass)


def texImage2D(target, level, internalformat, format, type, pixels):
    return PROXY["texImage2D"](target, level, internalformat, format, type, pixels)


def texParameterf(target, pname, param):
    return PROXY["texParameterf"](target, pname, param)
def texParameteri(target, pname, param):
    return PROXY["texParameteri"](target, pname, param)


def texSubImage2D(target, level, xoffset, yoffset, format, type, pixels):
    return PROXY["texSubImage2D"](target, level, xoffset, yoffset, format, type, pixels)


def uniform1f(location, v1):
    return PROXY["uniform1f"](location, v1)
def uniform2f(location, v1, v2):
    return PROXY["uniform2f"](location, v1, v2)
def uniform3f(location, v1, v2, v3):
    return PROXY["uniform3f"](location, v1, v2, v3)
def uniform4f(location, v1, v2, v3, v4):
    return PROXY["uniform4f"](location, v1, v2, v3, v4)
def uniform1i(location, v1):
    return PROXY["uniform1i"](location, v1)
def uniform2i(location, v1, v2):
    return PROXY["uniform2i"](location, v1, v2)
def uniform3i(location, v1, v2, v3):
    return PROXY["uniform3i"](location, v1, v2, v3)
def uniform4i(location, v1, v2, v3, v4):
    return PROXY["uniform4i"](location, v1, v2, v3, v4)
def uniform1fv(location, count, values):
    return PROXY["uniform1fv"](location, count, values)
def uniform2fv(location, count, values):
    return PROXY["uniform2fv"](location, count, values)
def uniform3fv(location, count, values):
    return PROXY["uniform3fv"](location, count, values)
def uniform4fv(location, count, values):
    return PROXY["uniform4fv"](location, count, values)
def uniform1iv(location, count, values):
    return PROXY["uniform1iv"](location, count, values)
def uniform2iv(location, count, values):
    return PROXY["uniform2iv"](location, count, values)
def uniform3iv(location, count, values):
    return PROXY["uniform3iv"](location, count, values)
def uniform4iv(location, count, values):
    return PROXY["uniform4iv"](location, count, values)


def uniformMatrix2fv(location, count, transpose, values):
    return PROXY["uniformMatrix2fv"](location, count, transpose, values)
def uniformMatrix3fv(location, count, transpose, values):
    return PROXY["uniformMatrix3fv"](location, count, transpose, values)
def uniformMatrix4fv(location, count, transpose, values):
    return PROXY["uniformMatrix4fv"](location, count, transpose, values)


def useProgram(program):
    return PROXY["useProgram"](program)


def validateProgram(program):
    return PROXY["validateProgram"](program)


def vertexAttrib1f(index, v1):
    return PROXY["vertexAttrib1f"](index, v1)
def vertexAttrib2f(index, v1, v2):
    return PROXY["vertexAttrib2f"](index, v1, v2)
def vertexAttrib3f(index, v1, v2, v3):
    return PROXY["vertexAttrib3f"](index, v1, v2, v3)
def vertexAttrib4f(index, v1, v2, v3, v4):
    return PROXY["vertexAttrib4f"](index, v1, v2, v3, v4)


def vertexAttribPointer(indx, size, type, normalized, stride, offset):
    return PROXY["vertexAttribPointer"](indx, size, type, normalized, stride, offset)


def viewport(x, y, width, height):
    return PROXY["viewport"](x, y, width, height)


