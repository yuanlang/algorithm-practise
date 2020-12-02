package com.yuan.trie;

import java.util.*;

/**
 * Created by pfliu on 2019/12/06.
 */
public class TNode {
    /**
     * ��ǰ�ڵ��ַ�
     */
    private char c;
    /**
     * ��ǰ �ڵ��Ӧ����
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
     * �� �����ַ� ��ӵ������б��С�
     * 
     * @param nodes ������ node �б�
     * @param c     �����ַ�
     * @return �����Ľڵ�
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
     * �� ��ǰ�ڵ� ���뵽������ �ڵ��б��С� ���� resize ��ʱ��ת�ƽڵ��б�
     * 
     * @param nodes �ڵ��б�
     * @param node  �����ڵ�
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
     * �� �����ַ� ���뵽��ǰ�ڵ���ӽڵ��С�
     * 
     * @param c �����ַ�
     * @return �����Ľڵ�
     */
    TNode addChild(char c) {
        // ��ʼ���ӽڵ��б�
        if (children == null) {
            children = new TNode[2];
        }

        // ���Բ���
        TNode node = add(children, c);
        if (node != null)
            return node;

        // resize
        // ת�ƽڵ��б��µ��ӽڵ��б���
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
     * ���ҵ�ǰ�ڵ���ӽڵ��б��У�char ���ڸ����ַ��Ľڵ�
     * @param c ���� char
     * @return ��Ӧ�Ľڵ�
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

