"""
    Chen Jiawei, The University of Tokyo
    The main function show how to make PBCs for x-uniaxial tensile
"""
import os

def main():
    # make empty container
    id = []
    xcoor = []
    ycoor = []
    zcoor = []

    # begin to read the inp file
    inp_dir = r"test.k"
    with open(inp_dir, 'r') as inp:
        line = inp.readline()
        while line:
            id.append(int(line.split()[0]))
            xcoor.append(float(line.split()[1]))
            ycoor.append(float(line.split()[2]))
            zcoor.append(float(line.split()[3]))
            line = inp.readline()
    inp.close()

    # check the data accuracy
    if len(id) == len(xcoor) == len(ycoor) == len(zcoor):
        print("the size of each container is accuracy")

    # find the maximum, minimum x,y,z
    max_xcoor = max(xcoor)
    min_xcoor = min(xcoor)
    max_ycoor = max(ycoor)
    min_ycoor = min(ycoor)
    max_zcoor = max(zcoor)
    min_zcoor = min(zcoor)

    # find the face points
    # +x face, -x face: plusXface, minusXface
    # +y face, -y face,
    # +z face, -z face,
    # +x+y line, -x+y line, +x-y line, -x-y line
    # +x+z line, -x+z line, +x-z line, -x-z line
    # +z+y line, -z+y line, +z-y line, -z-y line
    # +x+y+z edge, +x-y+z edge, +x+y-z edge, +x-y-z edge
    # -x+y+z edge, -x-y+z edge, -x+y-z edge, -x-y-z edge
    # for example, +x face and -x face
    pXface, mXface, pYface, mYface, pZface, mZface = [], [], [], [], [], []
    pXpYline, pXmYline, pXpZline, pXmZline = [], [], [], []
    mXpYline, mXmYline, mXpZline, mXmZline = [], [], [], []
    pYpZline, pYmZline = [], []
    mYpZline, mYmZline = [], []
    for i in range(len(id)):
        # for points in +x face
        if xcoor[i] == max_xcoor:
            if ycoor[i] != max_ycoor and ycoor[i] != min_ycoor and zcoor[i] != max_zcoor and zcoor[i] != min_zcoor:
                pXface.append(i)
            if zcoor[i] != max_zcoor and zcoor[i] != min_zcoor:
                if ycoor[i] == max_ycoor:
                    pXpYline.append(i)
                if ycoor[i] == min_ycoor:
                    pXmYline.append(i)
            if ycoor[i] != max_ycoor and ycoor[i] != min_ycoor:
                if zcoor[i] == max_zcoor:
                    pXpZline.append(i)
                if zcoor[i] == min_zcoor:
                    pXmZline.append(i)

        # for points in -x face
        if xcoor[i] == min_xcoor:
            if ycoor[i] != max_ycoor and ycoor[i] != min_ycoor and zcoor[i] != max_zcoor and zcoor[i] != min_zcoor:
                mXface.append(i)
            if zcoor[i] != max_zcoor and zcoor[i] != min_zcoor:
                if ycoor[i] == max_ycoor:
                    mXpYline.append(i)
                if ycoor[i] == min_ycoor:
                    mXmYline.append(i)
            if ycoor[i] != max_ycoor and ycoor[i] != min_ycoor:
                if zcoor[i] == max_zcoor:
                    mXpZline.append(i)
                if zcoor[i] == min_zcoor:
                    mXmZline.append(i)

        # for points in +y face
        if ycoor[i] == max_ycoor:
            if xcoor[i] != max_xcoor and xcoor[i] != min_xcoor and zcoor[i] != max_zcoor and zcoor[i] != min_zcoor:
                pYface.append(i)
            if xcoor[i] != max_xcoor and xcoor[i] != min_xcoor:
                if zcoor[i] == max_zcoor:
                    pYpZline.append(i)
                if zcoor[i] == min_zcoor:
                    pYmZline.append(i)

        # for points in -y face
        if ycoor[i] == min_ycoor:
            if xcoor[i] != max_xcoor and xcoor[i] != min_xcoor and zcoor[i] != max_zcoor and zcoor[i] != min_zcoor:
                mYface.append(i)
            if xcoor[i] != max_xcoor and xcoor[i] != min_xcoor:
                if zcoor[i] == max_zcoor:
                    mYpZline.append(i)
                if zcoor[i] == min_zcoor:
                    mYmZline.append(i)

        # for points in +z face
        if zcoor[i] == max_zcoor:
            if ycoor[i] != max_ycoor and ycoor[i] != min_ycoor and xcoor[i] != max_xcoor and xcoor[i] != min_xcoor:
                pZface.append(i)

        # for points in -z face
        if zcoor[i] == min_zcoor:
            if ycoor[i] != max_ycoor and ycoor[i] != min_ycoor and xcoor[i] != max_xcoor and xcoor[i] != min_xcoor:
                mZface.append(i)

        # edge point
        if xcoor[i] == max_xcoor and ycoor[i] == max_ycoor and zcoor[i] == max_zcoor:
            pXpYpZpoint = i
        if xcoor[i] == max_xcoor and ycoor[i] == min_ycoor and zcoor[i] == max_zcoor:
            pXmYpZpoint = i
        if xcoor[i] == max_xcoor and ycoor[i] == min_ycoor and zcoor[i] == min_zcoor:
            pXmYmZpoint = i
        if xcoor[i] == max_xcoor and ycoor[i] == max_ycoor and zcoor[i] == min_zcoor:
            pXpYmZpoint = i
        if xcoor[i] == min_xcoor and ycoor[i] == max_ycoor and zcoor[i] == max_zcoor:
            mXpYpZpoint = i
        if xcoor[i] == min_xcoor and ycoor[i] == min_ycoor and zcoor[i] == max_zcoor:
            mXmYpZpoint = i
        if xcoor[i] == min_xcoor and ycoor[i] == min_ycoor and zcoor[i] == min_zcoor:
            mXmYmZpoint = i
        if xcoor[i] == min_xcoor and ycoor[i] == max_ycoor and zcoor[i] == min_zcoor:
            mXpYmZpoint = i

    # begin to check the correspond point
    setid = 1
    inp_dir = r"new.k"
    os.remove(inp_dir)
    # +x and -x
    constrList = [2,3]
    setFacePBC(inp_dir,setid,pXface,mXface,ycoor,zcoor,constrList,id)
    # +y and -y
    constrList = [1,2,3]
    setFacePBC(inp_dir,setid,pYface,mYface,xcoor,zcoor,constrList,id)
    # +z and -z
    constrList = [1, 2, 3]
    setFacePBC(inp_dir, setid, pZface, mZface, xcoor, zcoor, constrList, id)
    # +x+y line -x+y line
    constrList = [2, 3]
    setLinePBC(inp_dir,setid,pXpYline,mXpYline,zcoor,constrList,id)
    # +x-y line and -x-y line
    constrList = [2, 3]
    setLinePBC(inp_dir, setid, pXmYline, mXmYline, zcoor, constrList, id)
    # +x+z line and -x+z line
    constrList = [2, 3]
    setLinePBC(inp_dir, setid, pXpZline, mXpZline, ycoor, constrList, id)
    # +x-z line and -x-z line
    constrList = [2, 3]
    setLinePBC(inp_dir, setid, pXmZline, mXmZline, ycoor, constrList, id)
    # +y+z line and -y+z line
    constrList = [1, 2, 3]
    setLinePBC(inp_dir, setid, pYpZline, mYpZline, xcoor, constrList, id)
    # +y-z line and -y-z line
    constrList = [1, 2, 3]
    setLinePBC(inp_dir, setid, pYmZline, mYmZline, xcoor, constrList, id)

    # edge
    constrList = [2, 3]
    setPointPBC(inp_dir,setid,pXpYpZpoint,mXpYpZpoint,constrList,id)
    setPointPBC(inp_dir, setid, pXmYpZpoint, mXmYpZpoint, constrList,id)
    setPointPBC(inp_dir, setid, pXpYmZpoint, mXpYmZpoint, constrList,id)
    setPointPBC(inp_dir, setid, pXmYmZpoint, mXmYmZpoint, constrList,id)

"""
    functions
"""
def calDistance2D(onecoor1,onecoor2,twocoor1,twocoor2):
    val = pow(pow(onecoor1-twocoor1,2) + pow(onecoor2-twocoor2,2),0.5)
    return val

def setFacePBC(inp_dir,setid, faceOne, faceTwo, chkCoorOne, chkCoorTwo, constrList,nodeidList):
    for i in faceOne:
        distance = 1.0
        target = 0
        for j in faceTwo:
            val = calDistance2D(chkCoorOne[i], chkCoorTwo[i], chkCoorOne[j], chkCoorTwo[j])
            if distance > val:
                target = j
                distance = val
        for dir in constrList:
            setid += formatWritePBCOneSet(inp_dir, setid, nodeidList[i], nodeidList[target], dir)

def setLinePBC(inp_dir,setid, lineOne, lineTwo, chkCoor, constrList,nodeidList):
    for i in lineOne:
        distance = 1.0
        target = 0
        for j in lineTwo:
            val = abs(chkCoor[i] - chkCoor[j])
            if distance > val:
                target = j
                distance = val
        for dir in constrList:
            setid += formatWritePBCOneSet(inp_dir, setid, nodeidList[i], nodeidList[target], dir)

def setPointPBC(inp_dir,setid,pointOne,pointTwo,constrList,nodeidList):
    for dir in constrList:
        setid += formatWritePBCOneSet(inp_dir, setid, nodeidList[pointOne], nodeidList[pointTwo], dir)

def formatWritePBCOneSet(inp_dir,setid,nodeOneId,nodeTwoId,constrCoor):
    with open(inp_dir, 'a') as inp:
        inp.write("*CONSTRAINED_LINEAR_GLOBAL\n")
        inp.write(f"{setid}\n".rjust(11))
        inp.write(f"{nodeOneId}".rjust(10))
        inp.write(f"{constrCoor}".rjust(10))
        inp.write("       1.0\n")
        inp.write(f"{nodeTwoId}".rjust(10))
        inp.write(f"{constrCoor}".rjust(10))
        inp.write("      -1.0\n")
        inp.close()
    return 1

if __name__ == '__main__':
    main()

