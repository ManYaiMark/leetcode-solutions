class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        n_list = []

        def generate(open_count, close_count, path):
            if len(path) == n * 2 :
                n_list.append(path)
                
                return 
            
            if open_count < n :
                generate(open_count+1,close_count,path+'(') 

            if close_count < open_count :
                generate(open_count,close_count+1,path+')')


        generate(0,0,'')

        return n_list
