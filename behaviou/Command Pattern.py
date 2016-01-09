#-*- coding:utf-8 -*-
# 作者 --- 李秋生
# 项目名称 --- 命令模式
'''
  命令模式 (Command Pattern) 可以把命令封装成对象, 这样的话 就可以构建命令序列, 以便稍后执行,
  或者创建可撤销的命令
'''
from __future__ import print_function

# 首先 创建一个空的格子集合

class Grid:
    '''
     创建 Grid类, 保存颜色名称所用的二维表格
    '''
    def __init__(self,width,height):
        self._cell = [['white' for _ in range(width)] for _ in range(height)]
    # cell 是setter,也是一个getter,分别设置和获取[x,y] = color
    # 如果color不为空,则通过则通过该color值设置x和y对应的cell值;
    # 否则,_cell 函数getter,获取cell[x,y] = color

    def cell(self, x, y, color=None):
        if color:
             self._cell[x][y] = color
        else:
            return self._cell[x][y]

    # Python内置的@property装饰器就是负责把一个方法变成属性调用
    # 获取高度 只读属性
    @property
    def height(self):
        return len(self._cell)

    # 获取宽度 只读属性
    @property
    def width(self):
        return len(self._cell[0])

    # 打印所有信息
    def print_info(self):
        print("cells:")
        for x in range(self.width):
                print(self._cell[x])

# 为了使Grid支持撤销功能, 创建子类, 并向其中添加两个方法
class UndoGrid(Grid):
    # 每个cell都有撤销和增加功能 (属于原子操作)
    def create_cell_command(self,x,y,color):
        def undo():
            self.cell(x,y,undo.color)

        def do():
            undo.color = self.cell(x,y)
            if undo.color == color:
                pass
            else:
                self.cell(x,y,color)

        return Command(do,undo,'Cell')

    def create_rectangle_macro(self,x0,y0,x1,y1,color):
        macro = Macro("Rectangle")
        for x in range(x0,x1+1):
            for y in range(y0,y1+1):
                macro.add(self.create_cell_command(x,y,color))

        return macro

# Command
class Command:

    def __init__(self,do,undo,description):
        assert callable(do) and callable(undo)
        self.do = do
        self.undo = undo
        self.description = description

    # call 方法
    def __call__(self):
        self.do()

# Macro 宏功能: 可批量完成 添加命令和逆序删除命令

class Macro:
    def __init__(self,description=""):
        self.description = description
        self._commands = []

    def add(self,command):
        if not isinstance(command,Command):
            raise TypeError("Expect object of type Command{}".format(type(command).__name__))
        self._commands.append(command)

    # call
    def __call__(self):
        for command in self._commands:
            command()

    def do(self):
        do = self.__call__

    def undo(self):
        for command in reversed(self._commands):
            command.undo()

if __name__ == "__main__":
    grid = UndoGrid(4,5)
    redleft = grid.create_cell_command(0,0,'red')
    redright = grid.create_cell_command(2,1,'red')
    # redleft do()
    redleft()  # 1
    redright.do()  # 2 do 1 和 2是等价的
    grid.print_info() # look information do之后查看信息
    redleft.undo() # 1 undo
    grid.print_info() # look information undo之后查看信息 对比

    # UndoGrid



