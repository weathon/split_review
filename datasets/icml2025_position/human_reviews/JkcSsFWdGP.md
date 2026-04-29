## Human Reviewer 1

### Questions
---

### Rating
3

### Confidence
3

---

## Human Reviewer 2

### Questions
Do you think the field of Spectral GNNs has misinterpreted or oversimplified these prior results?

What are some specific misconceptions that need to be corrected in future research?

Should we abandon spectral filtering approaches altogether, or is there a way to redefine them in a more theoretically sound way? Could alternative graph dictionaries (as you mention) provide a better foundation? What would be a good starting point for exploring them?

### Rating
3

### Confidence
5

---

## Human Reviewer 3

### Questions
1. In Section 4.6, the authors mention the trade-off between expressiveness and generalizability as a key concern in spectral GNNs. Could the authors provide concrete examples or scenarios where this trade-off becomes a more pressing issue in spectral GNNs, especially in contrast to classical Fourier analysis?
2. In Section 3.4, the authors argue that low-frequency eigenvectors are widely used in practice, and that spectral graphs often work well in practical domains. If that is the case, why is the issue with GFBs problematic in real-world scenarios?  Graphs with well-behaved eigenvectors do not seem to be a "special" case from a practical perspective, otherwise issues related to the limitations of GFB would have already manifested more prominently. Could the authors provide examples where GFB directly leads to performance degradation or instability in practical tasks?
3. Regarding Theorems 4.2, 4.4, and 4.6, it makes sense that having small $C$, $K$, and $\alpha$ leads to small upper bounds and better stability, the converse is not necessarily true. Could there be cases where the system remains stable despite the theoretical upper bound being large? When and why do such upper bounds become tight, thereby harming stability and generalization of spectral GNNs?

### Rating
3

### Confidence
3