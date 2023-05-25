import unittest
import sys
import os

# __file__ 是当前文件的路径
# os.path.dirname() 获取一个路径的目录部分
# os.path.abspath() 将相对路径转化为绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 如果你的测试脚本在项目根目录下的tests/子目录中，你可能需要返回上一级目录来获取项目的根目录
root_dir = os.path.dirname(current_dir)

# 将项目的根目录添加到 sys.path
sys.path.insert(0, root_dir)
 
from eastmoney import f10


class TestShareholderResearch(unittest.TestCase):
    def test_shareholder_research(self):
        result = f10.shareholder_research('SH603288')
        self.assertIsInstance(result, dict)
        self.assertIn('gdrs', result)
        self.assertIn('sdltgd_date', result)
        self.assertIn('sdgd_date', result)
        self.assertIn('sjkzr', result)
        self.assertIn('jgcc_date', result)
        self.assertIn('sdgdcgbd', result)
        self.assertIn('jjcg_date', result)
        self.assertIn('xsjj', result)
        self.assertIn('sdltgd', result)
        self.assertIn('ltgf', result)
        self.assertIn('sdgd', result)
        self.assertIn('jgcc', result)
        self.assertIn('jjcg', result)

if __name__ == '__main__':
    unittest.main()
