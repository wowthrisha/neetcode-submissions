class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        r=0
        
        for c in tokens:
            if len(tokens)<=1:
                return int(c)
            if c not in "+-*/":
                stack.append(c)
            else:
                if stack:
                    a=int(stack.pop())
                if stack:
                    b=int(stack.pop())
           
                if c=="+":
                    r=(a+b)
                elif c=="-":
                    r=(b-a)
                elif c=="*":
                    r=(a*b)
                elif c=="/":
                    if b==0:
                        print("zero div error")
                        
                    else:
                        r=(b/a)
                else:
                    print("no")
                stack.append(int(r))
        return int(r)
            