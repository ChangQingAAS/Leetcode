var connect = function(root) {
    BFS(root)
    return root;
};

let BFS = function(root){
    if(root == null){
        return;
    }
    let nodes = [];

    nodes.push(root);
    while(nodes.length != 0 ){
        // for-loop 每一层，用索引长度结束当前层
        let line_length = nodes.length;
        for(let i = 0; i <line_length; i++){
            let cur_node = nodes.shift();
            if(i != line_length - 1 )
                cur_node.next = nodes[0];
            else    
                cur_node.next = null;
            
            if(cur_node.right != null)
            {
                nodes.push(cur_node.left);
                nodes.push(cur_node.right);
            }
        }
    }
}