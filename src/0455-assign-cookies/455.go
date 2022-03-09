func findContentChildren(g []int, s []int) int {
    sort.Ints(g)
    sort.Ints(s)
    g_index, s_index,result := 0, 0, 0
    for g_index < len(g) && s_index < len(s){
        if g[g_index] <= s[s_index]{
            result ++
            g_index ++
        }
        s_index++
    }
    return result
}