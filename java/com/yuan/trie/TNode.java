package com.yuan.trie;

import java.util.*;

/**
 * Created by pfliu on 2019/12/06.
 */
public class TNode {
    /**
     * 当前节点字符
     */
    private char c;
    /**
     * 当前 节点对应数字
     */
    int count = 0;

    private TNode[] children;

    private static int hash(char c) {
        return c;
    }

    @Override
    public String toString() {
        return "TNode{" + "c=" + c + ", count=" + count + ", children=" + Arrays.toString(children) + '}';
    }

    TNode(char c) {
        this.c = c;
    }

    /**
     * 将 给定字符 添加到给定列表中。
     * 
     * @param nodes 给定的 node 列表
     * @param c     给定字符
     * @return 插入后的节点
     */
    private static TNode add(final TNode[] nodes, char c) {
        int hash = hash(c);
        int mask = nodes.length - 1;

        for (int i = hash; i < hash + mask + 1; i++) {
            int idx = i & mask;
            if (nodes[idx] == null) {
                TNode node = new TNode(c);
                nodes[idx] = node;
                return node;
            } else if (nodes[idx].c == c) {
                return nodes[idx];
            }
        }
        return null;
    }

    /**
     * 将 当前节点 放入到给定的 节点列表中。 用于 resize 的时候转移节点列表
     * 
     * @param nodes 节点列表
     * @param node  给定节点
     */
    private static void add(final TNode[] nodes, TNode node) {
        int hash = hash(node.c);
        int len = nodes.length - 1;

        for (int i = hash; i < hash + len + 1; i++) {
            int idx = i & len;
            if (nodes[idx] == null) {
                nodes[idx] = node;
                return;
            } else if (nodes[idx].c == node.c) {
                throw new IllegalStateException("Node not expected for " + node.c);
            }
        }
        throw new IllegalStateException("Node not added");
    }

    /**
     * 将 给定字符 插入到当前节点的子节点中。
     * 
     * @param c 给定字符
     * @return 插入后的节点
     */
    TNode addChild(char c) {
        // 初始化子节点列表
        if (children == null) {
            children = new TNode[2];
        }

        // 尝试插入
        TNode node = add(children, c);
        if (node != null)
            return node;

        // resize
        // 转移节点列表到新的子节点列表中
        TNode[] tmp = new TNode[children.length * 2];
        for (TNode child : children) {
            if (child != null) {
                add(tmp, child);
            }
        }

        children = tmp;
        return add(children, c);
    }

    /**
     * 查找当前节点的子节点列表中，char 等于给定字符的节点
     * @param c 给定 char
     * @return 对应的节点
     */
    TNode findChild(char c) {
        final TNode[] nodes = children;
        if (nodes == null) return null;

        int hash = hash(c);
        int len = nodes.length - 1;

        for (int i = hash; i < hash + len + 1; i++) {
            int idx = i & len;
            TNode node = nodes[idx];
            if (node == null) {
                return null;
            } else if (node.c == c) {
                return node;
            }
        }
        return null;
    }
}

