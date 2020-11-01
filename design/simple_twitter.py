#!/usr/bin/python
# -*- coding: GBK -*-

# Twitter twitter = new Twitter();

# // �û�1������һ�������� (�û�id = 1, ����id = 5).
# twitter.postTweet(1, 5);

# // �û�1�Ļ�ȡ����Ӧ������һ���б����а���һ��idΪ5������.
# twitter.getNewsFeed(1);

# // �û�1��ע���û�2.
# twitter.follow(1, 2);

# // �û�2������һ�������� (����id = 6).
# twitter.postTweet(2, 6);

# // �û�1�Ļ�ȡ����Ӧ������һ���б����а����������ģ�id�ֱ�Ϊ -> [6, 5].
# // ����id6Ӧ��������id5֮ǰ����Ϊ������5֮���͵�.
# twitter.getNewsFeed(1);

# // �û�1ȡ����ע���û�2.
# twitter.unfollow(1, 2);

# // �û�1�Ļ�ȡ����Ӧ������һ���б����а���һ��idΪ5������.
# // ��Ϊ�û�1�Ѿ����ٹ�ע�û�2.
# twitter.getNewsFeed(1);

# ��Դ�����ۣ�LeetCode��
# ���ӣ�https://leetcode-cn.com/problems/design-twitter
# ����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

from collections import deque
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #key user_id, value twitter_ids
        self.twitter_users = dict()
        #key user_id, value follow_user_id
        self.twitter_follow = dict()
        #record the sequence of twitters, 0 indicate the earliest
        # ��dict����queue���Լӿ��ٶ�
        self.twitter_dict = dict()
        self.internal_index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.twitter_users:
            self.twitter_users[userId] = list()
        self.twitter_users[userId].append(tweetId)
        self.twitter_dict[tweetId] = self.internal_index
        # print(self.twitter_dict)
        self.internal_index += 1

    def getTwitterTimeIndex(self, twitterId1) -> bool:
        """
        ��ȡ��twitter_queue�е�λ��
        """
        index = self.twitter_dict[twitterId1]
        # print("twitterId = ", twitterId1, "index = ", index)
        return index

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        result = []
        #��ȡ�Լ�����Ϣ�б�
        if userId in self.twitter_users:
            result = list(self.twitter_users[userId])
        #��ȡfollow�û�����Ϣ�б�
        if userId not in self.twitter_follow:
            #һ���˷���twitter������Ǳ���ģ�ֻ��Ҫ��ת����
            sorted_list = result[::-1]
            # ֻȡǰ10
            return sorted_list[:10]
        follow_list = list(self.twitter_follow[userId])
        for user_id in follow_list:
            if user_id in self.twitter_users:
                result += list(self.twitter_users[user_id])
        #�����ɽ���Զ
        sorted_list = sorted(result, key=self.getTwitterTimeIndex, reverse=True)
        # ֻȡǰ10
        return sorted_list[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # �����ע�Լ������
        if followerId == followeeId:
            return
        if followerId not in self.twitter_follow:
            self.twitter_follow[followerId] = list()
        # �����ظ���ע�����
        if followeeId not in self.twitter_follow[followerId]:
            self.twitter_follow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        #����followerId�����ڵ����
        if followerId not in self.twitter_follow:
            return None
        # ����followeeId����followerId list�����
        if followeeId not in self.twitter_follow[followerId]:
            return None
        index = self.twitter_follow[followerId].index(followeeId)
        del(self.twitter_follow[followerId][index])


if __name__ == "__main__":
    #Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    userId = 1
    tweetId = 5
    obj.postTweet(userId,tweetId)
    param_2 = obj.getNewsFeed(userId)
    print(param_2)

    followerId = 1
    followeeId = 2
    obj.follow(followerId, followeeId)
    
    userId = 2
    tweetId = 6
    obj.postTweet(userId, tweetId)
    userId = 1
    param_2 = obj.getNewsFeed(userId)
    print(param_2)

    obj.unfollow(followerId, followeeId)
    param_2 = obj.getNewsFeed(userId)
    print(param_2)
