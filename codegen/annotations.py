import ctypes

## bind / gen / delete stuff

def bindAttribLocation(program, index, name):
    name = ctypes.c_char_p(name.encode('utf-8'))  # desktop angle
    ()  # desktop angle


def deleteBuffer(buffer):
    n = 1
    buffers = (ctypes.c_uint*n)(buffer)  # desktop angle
    ()  # desktop angle

def deleteFramebuffer(framebuffer):
    n = 1
    buffers = (ctypes.c_uint*n)(framebuffer)  # desktop angle
    ()  # desktop angle

def deleteRenderbuffer(renderbuffer):
    n = 1
    buffers = (ctypes.c_uint*n)(renderbuffer)  # desktop angle
    ()  # desktop angle

def deleteTexture(texture):
    n = 1
    buffers = (ctypes.c_uint*n)(texture)  # desktop angle
    ()  # desktop angle


def createBuffer():
    n = 1
    buffers = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return buffers[0]  # desktop angle

def createFramebuffer():
    n = 1
    framebuffers = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return framebuffers[0]  # desktop angle

def createRenderbuffer():
    n = 1
    renderbuffers = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return renderbuffers[0]  # desktop angle

def createTexture():
    n = 1
    textures = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return textures[0]  # desktop angle

# def deleteBuffers(*buffers):
#     n = len(buffers)  # desktop angle
#     buffers = (ctypes.c_uint*n)(*buffers)  # desktop angle
#     ()  # desktop angle
# 
# def deleteFramebuffers(*framebuffers):
#     n = len(framebuffers)  # desktop angle
#     buffers = (ctypes.c_uint*n)(*framebuffers)  # desktop angle
#     ()  # desktop angle
# 
# def deleteRenderbuffers(*renderbuffers):
#     n = len(renderbuffers)  # desktop angle
#     buffers = (ctypes.c_uint*n)(*renderbuffers)  # desktop angle
#     ()  # desktop angle
# 
# def deleteTextures(*textures):
#     n = len(textures)  # desktop angle
#     buffers = (ctypes.c_uint*n)(*textures)  # desktop angle
#     ()  # desktop angle
# 
# 
# def genBuffers(n) -> tuple:
#     buffers = (ctypes.c_uint*n)()  # desktop angle
#     ()  # desktop angle
#     return tuple(buffers)  # desktop angle
# 
# def genFramebuffers(n) -> tuple:
#     framebuffers = (ctypes.c_uint*n)()  # desktop angle
#     ()  # desktop angle
#     return tuple(framebuffers)  # desktop angle
# 
# def genRenderbuffers(n) -> tuple:
#     renderbuffers = (ctypes.c_uint*n)()  # desktop angle
#     ()  # desktop angle
#     return tuple(renderbuffers)  # desktop angle
# 
# def genTextures(n) -> tuple:
#     textures = (ctypes.c_uint*n)()  # desktop angle
#     ()  # desktop angle
#     return tuple(textures)  # desktop angle


## Image stuff

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
    ()


def texSubImage2D(target, level, xoffset, yoffset, format, type, pixels):
    if not pixels.flags['C_CONTIGUOUS']:
        pixels = pixels.copy('C')
    pixels_ = pixels
    pixels = pixels_.ctypes.data
    width, height = pixels_.shape[:2]
    ()


def readPixels(x, y, width, height, format, type):
    """ Return pixels as bytes.
    """
    size = width*height
    pixels = (ctypes.c_uint8*size)()
    ()
    return bytes(pixels)


def compressedTexImage2D(target, level, internalformat, width=0, height=0, border=0, data=None):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.size
    data = data_.ctypes.data
    ()

def compressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, data):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.size
    data = data_.ctypes.data
    ()


## Buffer data

# todo: Also test for ALIGNED?

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
    ()


def bufferSubData(target, offset, data):
    if not data.flags['C_CONTIGUOUS']:
        data = data.copy('C')
    data_ = data
    size = data_.nbytes
    data = data_.ctypes.data
    ()


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
    ()


# todo: not so sure about this one
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
    ()


## Setters


def shaderSource(shader, *strings):
    if len(strings) == 1 and isinstance(strings[0], (tuple, list)):
        strings = strings[0]
    count = len(strings)  # desktop angle
    string = (ctypes.c_char_p*count)(*[s.encode('utf-8') for s in strings])  # desktop angle
    length = (ctypes.c_int*count)(*[len(s) for s in strings])  # desktop angle
    ()  # desktop angle


## Getters

def getString(pname):
    ()
    return res.value

def getActiveAttrib(program, index):
    bufsize = 256
    length = (ctypes.c_int*1)()
    size = (ctypes.c_int*1)()
    type = (ctypes.c_uint*1)()
    name = ctypes.create_string_buffer(bufsize)
    ()
    name = name[:length[0]].decode('utf-8')
    return name, size[0], type[0]


def getVertexAttribPointerv(index, pname):
    pointer = (ctypes.c_void_p*1)()
    ()
    return pointer[0]

    
def getActiveUniform(program, index):
    bufsize = 256
    length = (ctypes.c_int*1)()
    size = (ctypes.c_int*1)()
    type = (ctypes.c_uint*1)()
    name = ctypes.create_string_buffer(bufsize)
    ()
    name = name[:length[0]].decode('utf-8')
    return name, size[0], type[0]


def getAttachedShaders(program):
    maxcount = 256
    count = (ctypes.c_int*1)()
    shaders = (ctypes.c_uint*1)()
    ()
    return tuple(shaders[:count[0]])


def getAttribLocation(program, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    ()
    return res

def getUniformLocation(program, name):
    name = ctypes.c_char_p(name.encode('utf-8'))
    ()
    return res


def getProgramInfoLog(program):
    bufsize = 1024
    length = (ctypes.c_int*1)()
    infolog = ctypes.create_string_buffer(bufsize)
    ()
    return infolog[:length[0]].decode('utf-8')

def getShaderInfoLog(shader):
    bufsize = 1024
    length = (ctypes.c_int*1)()
    infolog = ctypes.create_string_buffer(bufsize)
    ()
    return infolog[:length[0]].decode('utf-8')

def getBooleanv(pname):
    data = (ctypes.c_bool*1)()
    ()
    return data[0]

def getFloatv(pname):
    data = (ctypes.c_float*1)()
    ()
    return data[0]

def getIntegerv(pname):
    data = (ctypes.c_int*1)()
    ()
    return data[0]

def getProgramiv(program, pname):
    params = (ctypes.c_int*1)()
    ()
    return params[0]

def getShaderiv(shader, pname):
    params = (ctypes.c_int*1)()
    ()
    return params[0]

def getShaderPrecisionFormat(shadertype, precisiontype):
    range = (ctypes.c_int*1)()
    precision = (ctypes.c_int*1)()
    ()
    return range[0], precision[0]

def getShaderSource(shader):
    bufSize = 1024*1024
    length = (ctypes.c_int*1)()
    source = (ctypes.c_char*bufsize)()
    ()
    return source.value[:length[0]].decode('utf-8')

def getBufferParameteriv(target, pname):
    data = (ctypes.c_int*1)()
    ()
    return data[0]


def getFramebufferAttachmentParameteriv(target, attachment, pname):
    params = (ctypes.c_int*1)()
    ()
    return params[0]

def getRenderbufferParameteriv(target, pname):
    params = (ctypes.c_int*1)()
    ()
    return params[0]




## ============================================================================


class FunctionAnnotation:
    def __init__(self, name, args, output):
        self.name = name
        self.args = args
        self.output = output
        self.lines = []  # (line, comment) tuples
    
    def __repr__(self):
        return '<FunctionAnnotation for %s>' % self.name
        
    def get_lines(self, call, backend):
        """ Get the lines for this function based on the given backend. 
        The given API call is inserted at the correct location.
        """
        lines = []
        for line, comment in self.lines:
            if (backend in comment) or (not comment):
                if line.strip() == '()':
                    line = call
                lines.append(line)
        return lines
    
    def is_arg_set(self, name):
        """ Get whether a given variable name is set.
        This allows checking whether a variable that is an input to the C
        function is not an input for the Python function, and may be an output.
        """
        needle = '%s =' % name
        for line, comment in self.lines:
            if line.startswith(needle):
                return True
        else:
            return False



def parse_anotations():
    """ Parse this annotations file and produce a dictionary of
    FunctionAnnotation objects.
    """
    
    functions = {}
    function = None
    
    for line in open(__file__, 'rt').readlines():
        # Stop?
        if '='*40 in line:
            break
        
        if line.startswith('def '):
            name = line.split(' ')[1].split('(')[0]
            args = line.split('(')[1].split(')')[0].split(', ')
            out =  line.partition('->')[2].strip()
            function = FunctionAnnotation(name, args, out)
            functions[name] = function
            continue
        elif not function:
            continue
        
        # Get line and comment
        comment = ''
        if '#' in line:
            line, comment = line.split('#', 1)
        line, comment = line.rstrip(), comment.strip()
        
        # Add line
        if line:
            function.lines.append((line,comment))

    return functions


if __name__ == '__main__':
    print(parse_anotations().keys())
    