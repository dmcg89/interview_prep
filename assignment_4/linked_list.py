def rotate(head_node, num):
  curr_node = head_node
  prev_node = None
  run = True
  while run:
    if curr_node.data == num:
      prev_node.next = None
      old_head = head_node
    if curr_node.next == None:
      curr_node.next = old_head
      return
    curr_node = curr_node.next
      
    