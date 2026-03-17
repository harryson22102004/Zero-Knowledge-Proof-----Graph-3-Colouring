Commitment Scheme: Commits to a random permutation of the 3-colouring using SHA-256, hiding actual colours from the
verifier.
Completeness & Soundness: Runs k rounds to drive soundness error below 2^(-k); verifier checks each revealed edge.
Algorithms Focus: Shows any NP problem has a ZKP by reduction to 3-colouring, establishing universality of the ZK
paradigm.
Tech Stack: Python, hashlib.
