class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hmap = {}
        for s in cpdomains:
            dots =  s.count(".")
            s = s.split()
            for _ in range(dots+1):
                hmap[s[1]] = hmap.get(s[1] , 0) + int(s[0])
                
                if "." in s[1]:
                    dot_indx = s[1].find(".")
                    s[1] = s[1][dot_indx+1:]
        return [f"{val} {key}" for key,val in hmap.items()]

        