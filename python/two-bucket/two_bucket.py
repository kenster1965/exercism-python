"""Two Bucket Problem"""
import math

def next_position(buckets: list, bucket_one: int, bucket_two: int):
    """Finds the next bucket combination.

    Args:
        buckets (list): Current state of the buckets [bucket 1, bucket 2].
        bucket_one (int): Capacity of bucket 1.
        bucket_two (int): Capacity of bucket 2.

    Return list: Updated bucket state after performing the next action.
    """
    if buckets[0] == 0:
        return [bucket_one, buckets[1]]  # Fill bucket 1

    if buckets[1] == bucket_two:
        return [buckets[0], 0]  # Empty bucket 2

    space_available = min(buckets[0], bucket_two - buckets[1])
    return [buckets[0] - space_available, buckets[1] + space_available]

def measure(bucket_one: int, bucket_two: int, goal: int, start_bucket: str):
    """How many times to get to the goal
        :params:
        bucket_one: int for size of bucket 1.
        bucket_two: int for size of bucket 2.
        goal: int - amount of water to reach in one of the buckets
        start_bucket: str - 'one' or 'two', which bucket to start with.

        :returns:
        steps: int  nb of iterations to get to the goal
        bucket_goal: str - which bucket has attained the volume goal
        rest: int - amount of water remaining in the other bucket
    """

    if math.gcd(bucket_one, bucket_two)>1 and goal % math.gcd(bucket_one, bucket_two) != 0:
        raise ValueError("Not possible.")
    if start_bucket not in {'one','two'}:
        raise ValueError("Wrong start_bucket.")
    if goal < 0 or goal > max(bucket_one, bucket_two):
        raise ValueError("The goal is unreachable.")
    steps = 1
    if start_bucket == "two":
        bucket_one, bucket_two = bucket_two, bucket_one
    buckets = [bucket_one, 0]
    if bucket_two==goal:
        steps+=1
        buckets[1]=bucket_two
    while goal not in buckets:
        steps += 1
        buckets = next_position(buckets, bucket_one, bucket_two)

    if start_bucket == "two":
        buckets = buckets[::-1]
    bucket_goal = "one" if buckets[0] == goal else "two"
    left_over = buckets[1] if bucket_goal == "one" else buckets[0]

    return steps, bucket_goal, left_over
