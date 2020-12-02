package com.yuan.trie;

import java.util.*;

/**
 * Created by pfliu on 2019/12/06.
 */
public class Trie {

    /**
     * ���ڵ�
     */
    final private TNode root = new TNode('\0');

    /**
     * ���һ���ʵ� Trie
     *
     * @param word  ����Ӵ�
     * @param value ��Ӧ value
     */
    public void addWord(String word, int value) {
        if (word == null || word.length() == 0)
            return;
        TNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            // ��ǰ char ��ӵ� trie �У����õ���ǰ char ��Ӧ���Ǹ��ڵ�
            node = node.addChild(c);
        }
        node.count = value;
    }

    /**
     * ���� word ��Ӧ�� int ֵ��
     *
     * @param word ���� word
     * @return ���һ���ڵ��ϴ洢�� int.
     */
    public int get(String word) {
        TNode node = root;
        for (int i = 0; i < word.length(); i++) {
            node = node.findChild(word.charAt(i));
            if (node == null) {
                return 0;
            }
        }
        return node.count;
    }

    private int get(char[] buffer, int offset, int length) {
        TNode node = root;
        for (int i = 0; i < length; i++) {
            node = node.findChild(buffer[offset + i]);
            if (node == null) {
                return 0;
            }
        }

        return node.count;
    }

    /**
     * �Ӹ����ַ����� offset ��ʼ�� �������ƥ��ĵ�һ�� int ֵ��
     *
     * @param str    �����ַ���
     * @param offset ��ʼ���ҵ�ƫ����
     * @return ��һ��ƥ����ַ��������һ���ڵ�� int ֵ��
     */
    public String maxMatch(String str, int offset) {
        TNode node = root;
        int lastMatchIdx = offset;

        for (int i = offset; i < str.length(); i++) {
            char c = str.charAt(i);
            node = node.findChild(c);
            if (node == null) {
                break;
            } else if (node.count != 0) {
                lastMatchIdx = i;
            }
        }
        return lastMatchIdx == offset ? null : str.substring(offset, lastMatchIdx + 1);
    }

    /**
     * �Ӹ����ַ����� offset <b>����</b>��ʼ�� �������ƥ��ĵ�һ�� int ֵ��
     *
     * @param str    �����ַ���
     * @param offset ��ʼ���ҵ�ƫ����
     * @return ��һ��ƥ����ַ��������һ���ڵ�� int ֵ��
     */
    public int maxMatchBack(String str, int offset) {
        TNode node = root;
        int lastMatchIdx = offset;

        for (int i = offset; i >= 0; i--) {
            char c = str.charAt(i);
            node = node.findChild(c);
            if (node == null) {
                break;
            } else if (node.count != 0) {
                lastMatchIdx = i;
            }
        }
        return offset - lastMatchIdx + 1;
    }

    /**
     * �Ӹ����ַ����� offset ��ʼ����� length ���ȡ� �������ƥ��ĵ�һ�� int ֵ��
     *
     * @param buffer �����ַ���
     * @param offset ��ʼ���ҵ�ƫ����
     * @return ��һ��ƥ����ַ��������һ���ڵ�� int ֵ��
     */
    public int maxMatch(char[] buffer, int offset, int length) {
        TNode node = root;
        int lastMatchIdx = offset;

        for (int i = offset; i < offset + length; i++) {
            char c = buffer[i];
            node = node.findChild(c);
            if (node == null) {
                break;
            } else if (node.count != 0) {
                lastMatchIdx = i;
            }
        }
        return lastMatchIdx - offset + 1;
    }

    public static void main(String[] args) {
        Trie trie = new Trie();

        for (String s : Arrays.asList("����", "���Ӷ�ʮ")) {
            trie.addWord(s, 1);
        }

        String input = "���Ӷ�ʮ����";

        System.out.println(trie.maxMatch(input, 0));

    }

}
