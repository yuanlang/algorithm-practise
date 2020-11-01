#!/usr/bin/python
# -*- coding: GBK -*-

# Twitter twitter = new Twitter();

# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
# twitter.postTweet(1, 5);

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# twitter.getNewsFeed(1);

# // 用户1关注了用户2.
# twitter.follow(1, 2);

# // 用户2发送了一个新推文 (推文id = 6).
# twitter.postTweet(2, 6);

# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# twitter.getNewsFeed(1);

# // 用户1取消关注了用户2.
# twitter.unfollow(1, 2);

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
# twitter.getNewsFeed(1);

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-twitter
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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
        # 用dict代替queue，以加快速度
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
        获取在twitter_queue中的位置
        """
        index = self.twitter_dict[twitterId1]
        # print("twitterId = ", twitterId1, "index = ", index)
        return index

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        result = []
        #获取自己的消息列表
        if userId in self.twitter_users:
            result = list(self.twitter_users[userId])
        #获取follow用户的消息列表
        if userId not in self.twitter_follow:
            #一个人发的twitter本身就是保序的，只需要倒转即可
            sorted_list = result[::-1]
            # 只取前10
            return sorted_list[:10]
        follow_list = list(self.twitter_follow[userId])
        for user_id in follow_list:
            if user_id in self.twitter_users:
                result += list(self.twitter_users[user_id])
        #排序，由近到远
        sorted_list = sorted(result, key=self.getTwitterTimeIndex, reverse=True)
        # 只取前10
        return sorted_list[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # 处理关注自己的情况
        if followerId == followeeId:
            return
        if followerId not in self.twitter_follow:
            self.twitter_follow[followerId] = list()
        # 处理重复关注的情况
        if followeeId not in self.twitter_follow[followerId]:
            self.twitter_follow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        #处理followerId不存在的情况
        if followerId not in self.twitter_follow:
            return None
        # 处理followeeId不在followerId list的情况
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
