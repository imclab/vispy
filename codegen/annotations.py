import ctypes

def bindAttribLocation(program, index, name):
    name = ctypes.c_char_p(name.encode('utf-8'))  # desktop angle
    ()  # desktop angle


def deleteBuffers(*buffers):
    n = len(buffers)  # desktop angle
    buffers = (ctypes.c_uint*n)(*buffers)  # desktop angle
    ()  # desktop angle

def deleteFramebuffers(*framebuffers):
    n = len(framebuffers)  # desktop angle
    buffers = (ctypes.c_uint*n)(*framebuffers)  # desktop angle
    ()  # desktop angle

def deleteRenderbuffers(*renderbuffers):
    n = len(renderbuffers)  # desktop angle
    buffers = (ctypes.c_uint*n)(*renderbuffers)  # desktop angle
    ()  # desktop angle

def deleteTextures(*textures):
    n = len(textures)  # desktop angle
    buffers = (ctypes.c_uint*n)(*textures)  # desktop angle
    ()  # desktop angle


def genBuffers(n) -> tuple:
    buffers = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return tuple(buffers)  # desktop angle

def genFramebuffers(n) -> tuple:
    framebuffers = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return tuple(framebuffers)  # desktop angle

def genRenderbuffers(n) -> tuple:
    renderbuffers = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return tuple(renderbuffers)  # desktop angle

def genTextures(n) -> tuple:
    textures = (ctypes.c_uint*n)()  # desktop angle
    ()  # desktop angle
    return tuple(textures)  # desktop angle


def shaderSource(shader, *strings):
    count = len(strings)  # desktop angle
    string = (ctypes.c_char_p*count)(*[s.encode('utf-8') for s in strings])  # desktop angle
    lengt = (ctypes.c_uint*count)(*[len(s) for s in strings])  # desktop angle
    ()  # desktop angle
    
    


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
        lines = []
        for line, comment in self.lines:
            if backend in comment:
                if line == '()':
                    line = call
                lines.append(line)
        return lines
    
    def is_set(self, name):
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
    """ Parse the annotations file and produce a dictionary of
    FunctionAnnotation objects.
    """
    
    functions = {}
    function = None
    
    for line in open(__file__, 'rt').readlines():
        # Stop?
        if line.startswith('##'):
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
        line, comment = line.strip(), comment.strip()
        
        # Add line
        if line:
            function.lines.append((line,comment))

    return functions


if __name__ == '__main__':
    print(parse_anotations().keys())
    