class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for p in paths:
            p = p.split() #p = ["root/a" , "1.txt(abcd)" , "2.txt(efgh)"]
            key = p[0]
            for i in range(1,len(p)):
                hmap[key].append(p[i]) #hmap = {"root/a" : ["1.txt(abcd)","2.txt(efgh)"]}
        
        '''
        paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        hmap = {"root/a" : ["1.txt(abcd)","2.txt(efgh)"] ,"root/c":["3.txt(abcd)"] , "root/c/d":["4.txt(efgh)"], "root":["4.txt(efgh)"]}
        '''
        hmap2 = defaultdict(list)
        for k,v in hmap.items():
            for i in range(len(v)):
                content_start_indx = v[i].find('(')
                content_end_indx = v[i].find(')')
                content = v[i][content_start_indx+1 : content_end_indx]
                hmap2[content].append(k+"/"+v[i][:content_start_indx])
            #hmap2={"abcd":["root/a/1.txt","root/c/3.txt"] "efgh":["root/a/2.txt" , "root/c/d/4.txt" , "root/4.txt" ]}
        ans = []
        for val in hmap2.values():
            if len(val)>1:
                ans.append(val)
        return ans       

