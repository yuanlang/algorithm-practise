package com.yuan.trie;

import java.util.*;

/**
 * Created by pfliu on 2019/12/06.
 */
public class Trie {

    /**
     * 根节点
     */
    final private TNode root = new TNode('\0');

    /**
     * 添加一个词到 Trie
     *
     * @param word  待添加词
     * @param value 对应 value
     */
    public void addWord(String word, int value) {
        if (word == null || word.length() == 0)
            return;
        TNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            // 当前 char 添加到 trie 中，并拿到当前 char 对应的那个节点
            node = node.addChild(c);
        }
        node.count = value;
    }

    /**
     * 查找 word 对应的 int 值。
     *
     * @param word 给定 word
     * @return 最后一个节点上存储的 int.
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
     * 从给定字符串的 offset 开始。 查找最大匹配的第一个 int 值。
     *
     * @param str    给定字符串
     * @param offset 开始查找的偏移量
     * @return 第一个匹配的字符串德最后一个节点的 int 值。
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
     * 从给定字符串的 offset <b>反向</b>开始。 查找最大匹配的第一个 int 值。
     *
     * @param str    给定字符串
     * @param offset 开始查找的偏移量
     * @return 第一个匹配的字符串德最后一个节点的 int 值。
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
     * 从给定字符串的 offset 开始。检查 length 长度。 查找最大匹配的第一个 int 值。
     *
     * @param buffer 给定字符串
     * @param offset 开始查找的偏移量
     * @return 第一个匹配的字符串德最后一个节点的 int 值。
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

        for (String s : Arrays.asList("呼延", "呼延二十")) {
            trie.addWord(s, 1);
        }

        String input = "呼延二十三四";

        System.out.println(trie.maxMatch(input, 0));

    }

}
