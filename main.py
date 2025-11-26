from collections import deque

def bfs_distances(graph, start):
    """
    Compute shortest distances from the start node to all reachable nodes using BFS.
    Returns a dict {node: distance}.
    """
    # If start node is missing, return empty dict
    if start not in graph:
        return {}

    # Initialize distances and queue
    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances