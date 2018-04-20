# -*-coding:utf-8 -*-
import sys
sys.setrecursionlimit(1000000)

class LongestPath():
  def __init__(self, node_map):
    self.node_map = node_map
    self.node_length = len(node_map)
    self.used_node_list = []
    self.collected_node_dict = {}
  def __call__(self, node):
    self.from_node = node[0]
    self.to_node = node[-1]
    self._init_longest()
    return self._format_path()
  def _init_longest(self):
    self.used_node_list.append(self.from_node)
    self.collected_node_dict[self.from_node] = [0, -1]
    # print self.used_node_list,self.collected_node_dict
    for index1, node1 in enumerate(self.node_map[self.from_node]):
      if node1>=0.0:
        # print index1,node1, self.from_node
        self.collected_node_dict[index1] = [node1, self.from_node]
    self._foreach_longest()
  def _foreach_longest(self):
    if len(self.used_node_list) == self.node_length - 1:
      return
    for index_iter, val in self.collected_node_dict.items(): # 遍历已有权值节点
      if index_iter not in self.used_node_list and index_iter != self.to_node:
        self.used_node_list.append(index_iter)
      else:
        continue
      self.inner_loop(index_iter)
    self._foreach_longest()
  def inner_loop(self,index_iter):
    for index, node in enumerate(self.node_map[index_iter]): # 对节点进行遍历
      # 如果节点在权值节点中并且权值大于新权值
      if node>=0 and index in self.collected_node_dict and self.collected_node_dict[index][0] < node + self.collected_node_dict[index_iter][0]:
        self.collected_node_dict[index][0] = node + self.collected_node_dict[index_iter][0] # 更新权值
        self.collected_node_dict[index][1] = index_iter
      elif node>=0 and index not in self.collected_node_dict:
        self.collected_node_dict[index] = [node + self.collected_node_dict[index_iter][0], index_iter]
      else:
        continue
      self.inner_loop(index)
  def _format_path(self):
    node_list = []
    critical_path= []
    collected_node_dict = self.collected_node_dict
    temp_node = self.to_node
    node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
    critical_path.append(temp_node)
    while self.collected_node_dict[temp_node][1] != -1:
      temp_node = self.collected_node_dict[temp_node][1]
      node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
      critical_path.append(temp_node)
    node_list.reverse()
    critical_path.reverse()
    return node_list,collected_node_dict,critical_path

if __name__ == "__main__":

  # node information
  node = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # adjacency matrix, if there is no contact, the weight is -1
  node_map = [[-1, 3.0, 0.0, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, 24, 25, 24.0, -1, -1, -1, -1, -1, -1], [-1, -1, -1, 47.0, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8], [-1, -1, -1, 71, -1, 72.0, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 10.0, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, 40.0, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, 42.0, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 18.0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

  longestpath = LongestPath(node_map)
  path = longestpath(node)
  print path