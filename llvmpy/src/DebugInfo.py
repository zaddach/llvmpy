from binding import *
from .namespace import llvm

from .ADT.StringRef import StringRef
from .Value import MDNode

DIDescriptor = llvm.Class()
DIEnumerator = llvm.Class(DIDescriptor)
DIScope = llvm.Class(DIDescriptor)
DIType = llvm.Class(DIScope)
DIBasicType = llvm.Class(DIType)
DIDerivedType = llvm.Class(DIType)
DICompositeType = llvm.Class(DIDerivedType)
DICompileUnit = llvm.Class(DIScope)
DIFile = llvm.Class(DIScope)
DIArray = llvm.Class(DIDescriptor)
DISubrange = llvm.Class(DIDescriptor)
DIGlobalVariable = llvm.Class(DIDescriptor)
DIVariable = llvm.Class(DIDescriptor)
DISubprogram = llvm.Class(DIScope)
DINameSpace = llvm.Class(DIScope)
DILexicalBlockFile = llvm.Class(DIScope)
DILexicalBlock = llvm.Class(DIScope)

llvm.includes.add('llvm/DebugInfo.h')

return_bool = cast(Bool, bool)
return_stringref = cast(StringRef, str)
return_unsigned = cast(Unsigned, int)

@DIDescriptor
class DIDescriptor:
    new = Constructor(ptr(MDNode))
    getTag = Method(return_unsigned)
    isDerivedType = Method(return_bool)
    isCompositeType = Method(return_bool)
    isBasicType = Method(return_bool)
    isVariable = Method(return_bool)
    isSubprogram = Method(return_bool)
    isGlobalVariable = Method(return_bool)
    isScope = Method(return_bool)
    isFile = Method(return_bool)
    isCompileUnit = Method(return_bool)
    isNameSpace = Method(return_bool)
    isLexicalBlockFile = Method(return_bool)
    isSubrange = Method(return_bool)
    isEnumerator = Method(return_bool)
    isType = Method(return_bool)
    isUnspecifiedParameter = Method(return_bool)
    isTemplateTypeParameter = Method(return_bool)
    isTemplateValueParameter = Method(return_bool)
    isObjCProperty = Method(return_bool)
    getMDNode = CustomMethod('DIDescriptor_getMDNode', PyObjectPtr)
    dump = Method(Void)
    delete = Destructor()

@DIScope
class DIScope:
    pass

@DICompileUnit
class DICompileUnit:
    new = Constructor(ptr(MDNode))
    getLanguage = Method(return_unsigned)
    getProducer = Method(return_stringref)
    isOptimized = Method(return_bool)
    getFlags = Method(return_stringref)
    getRunTimeVersion = Method(return_unsigned)
    getEnumTypes = Method(DIArray)
    getRetainedTypes = Method(DIArray)
    getSubprograms = Method(DIArray)
    getGlobalVariables = Method(DIArray)
    getImportedModules = Method(DIArray)
    getSplitDebugFilename = Method(return_stringref)

    Verify = Method(return_bool)
    delete = Destructor()

@DIFile
class DIFile:
    # getFileNode = Method(ptr(MDNode)) # not in LLVM 3.2?
    Verify = Method(return_bool)

@DIEnumerator
class DIEnumerator:
    getName = Method(return_stringref)
    getEnumValue = Method(cast(Uint64 if LLVM_VERSION <= (3, 3) else Int64, int))
    Verify = Method(return_bool)

@DIType
class DIType:
    getName = Method(return_stringref)
    getLineNumber = Method(return_unsigned)
    getSizeInBits = Method(return_unsigned)
    getAlignInBits = Method(return_unsigned)
    getOffsetInBits = Method(return_unsigned)
    getFlags = Method(return_unsigned)
    isPrivate = Method(return_bool)
    isProtected = Method(return_bool)
    isForwardDecl = Method(return_bool)
    isAppleBlockExtension = Method(return_bool)
    isBlockByrefStruct = Method(return_bool)
    isVirtual = Method(return_bool)
    isArtificial = Method(return_bool)
    isObjectPointer = Method(return_bool)
    isObjcClassComplete = Method(return_bool)
    isVector = Method(return_bool)
    isStaticMember = Method(return_bool)
    isValid = Method(return_bool)

    Verify = Method(return_bool)

@DIBasicType
class DIBasicType:
    pass

@DIDerivedType
class DIDerivedType:
    pass

@DICompositeType
class DICompositeType:
    pass

@DIArray
class DIArray:
    new = Constructor(ptr(MDNode))
    getNumElements = Method(return_unsigned)
    getElement = Method(DIDescriptor, cast(int, Unsigned))
    Verify = Method(return_bool)

@DISubrange
class DISubrange:
    Verify = Method(return_bool)

@DIGlobalVariable
class DIGlobalVariable:
    getContext = Method(DIScope)
    getName = Method(return_stringref)
    getDisplayName = Method(return_stringref)
    getLinkageName = Method(return_stringref)
    getType = Method(DIType)
    Verify = Method(return_bool)

@DIVariable
class DIVariable:
    Verify = Method(return_bool)

@DISubprogram
class DISubprogram:
    Verify = Method(return_bool)

@DINameSpace
class DINameSpace:
    Verify = Method(return_bool)

@DILexicalBlockFile
class DILexicalBlockFile:
    Verify = Method(return_bool)

@DILexicalBlock
class DILexicalBlock:
    Verify = Method(return_bool)

