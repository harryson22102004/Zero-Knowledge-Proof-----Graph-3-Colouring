import os, hashlib, random
 
def hash_commit(color, nonce):
    return hashlib.sha256(f"{color}:{nonce}".encode()).hexdigest()
 
def zkp_3colouring_round(coloring, graph_edges, permute=True):
    """One round of ZKP for 3-colouring (honest prover)."""
    colors=[0,1,2]
    if permute:
        perm={0:random.randint(0,2),1:random.randint(0,2),2:random.randint(0,2)}
        while len(set(perm.values()))<3: perm={0:random.randint(0,2),1:1,2:2}
    else:
        perm={0:0,1:1,2:2}
    permuted={v: perm[c] for v,c in coloring.items()}
    nonces={v:os.urandom(16).hex() for v in coloring}
    commitments={v:hash_commit(permuted[v],nonces[v]) for v in coloring}
    edge=random.choice(graph_edges)
    u,v=edge
    reveal={u:(permuted[u],nonces[u],commitments[u]),
            v:(permuted[v],nonces[v],commitments[v])}
    c_u,n_u,com_u=reveal[u]; c_v,n_v,com_v=reveal[v]
    verify_u=hash_commit(c_u,n_u)==com_u
    verify_v=hash_commit(c_v,n_v)==com_v
    valid=(c_u!=c_v) and verify_u and verify_v
    return valid
  graph_edges=[(0,1),(1,2),(2,0),(0,3),(1,4),(2,5)]
coloring={0:0,1:1,2:2,3:1,4:2,5:0}
results=[zkp_3colouring_round(coloring,graph_edges) for _ in range(20)]
print(f"ZKP rounds passed: {sum(results)}/20")
print(f"Soundness error per round: 1/|E| = 1/{len(graph_edges)}")
