class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> res = new ArrayList<>();
        int j;
        for(int i = left; i <= right; i++ )
        {
            // 不能改变i的值
            int num = i;
            // 1-9 加入结果集
            if(i>0 && i < 10)
            {
                res.add(num);
                continue;
            }

            //循环验证这个数
            while(num != 0)
            {
                //取个位数
                j = num % 10;
                //除数不能为0
                if(j == 0 || i % j != 0  )
                {
                    break;
                }
                //舍弃个位数
                num = num / 10;
            }

            //如果num 能够被整除到 0，说明满足以上判断条件，加入结果集
            if(num == 0)
                res.add(i);
            
        }
        return res;
    }
}