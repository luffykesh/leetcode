class Solution:
    def find(self,root, v1, path):
        if root == None:
            return False, ''
        if root.val == v1:
            return True, ''
        res, p = self.find(root.left, v1, path)
        if res:
            return True, 'L' + p
        
        res, p = self.find(root.right, v1, path)
        if res:
            return True, 'R' + p
        
        return False, ''

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res, rootToStart = self.find(root,startValue,'')
        res, rootToDest = self.find(root,destValue, '')
        
        i = 0
        while i != len(rootToStart) and i != len(rootToDest) and rootToStart[i] == rootToDest[i]:
            i += 1

        path = (len(rootToStart)-i)*'U' + rootToDest[i:]
        
        return path
