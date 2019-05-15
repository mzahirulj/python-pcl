from stl import mesh as m
import pcl.pcl_visualization as pv
import pcl
import os
import shutil as rm


# source file
mymesh = m.Mesh.from_file("C:/Users/tmp/test.stl")

def pclVisul(path):
    cloud = pcl.load(path)
    vis = pv.PCLVisualizering()
    vis.AddPointCloud(cloud)
    vis.Spin()
try:
    # temp directory
    currenDir = os.getcwd()
    temp_dir = currenDir + '\\tmp'

    if os.path.isdir(temp_dir):
        print('folder Exist')
    else:
        #Create new Directory
        os.mkdir(temp_dir)
    os.chdir(temp_dir)
    dst_file = 'tmp_file.pcd'
    dst_pcd = open(dst_file, 'w')

    stlVektor = mymesh.vectors
    numberOfLine = str(len(stlVektor))

    # header string
    header = ("# .PCD v0.7 - Point Cloud Data file format \n" +
              "VERSION 0.7 \n" +
              "FIELDS x y z \n" +
              "SIZE 4 4 4 \n" +
              "TYPE F F F \n" +
              "COUNT 1 1 1 \n" +
              "WIDTH " + numberOfLine + "\n" +
              "HEIGHT 1 \n" +
              "VIEWPOINT 0 0 0 1 0 0 0\n" +
              "POINTS " + numberOfLine + "\n" +
              "DATA ascii \n")
    dst_pcd.writelines(header)

    a = []
    for i in stlVektor:
        for k in i:
            a = str(k[0]) + " " + str(k[1]) + " " + str(k[2]) + "\n"
        dst_pcd.writelines(a)
    dst_pcd.close()

    # PCL Block
    pclVisul(dst_file)



except IOError:
    print('OOPS ')

finally:
    # todo temp_dir will be remove
    os.chdir(currenDir)
    rm.rmtree(temp_dir, ignore_errors=True)
    print('Created Folder Exist ! '+str (os.path.isdir(temp_dir)))
