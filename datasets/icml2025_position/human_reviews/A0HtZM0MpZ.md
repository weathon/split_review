## Human Reviewer 1

### Questions
- Concerning point (2): all the referenced papers seem to adopt very ad-hoc techniques to exploit the underlying sparsity (e.g., "layerwise stochastic coordinate descent"). What about pure SGD (or Adam), which is the default choice in practice?
- Also concerning point (2): for Transformers, even if a single attention layer is sparse (which is not true), the next one will process tokens that are weighted averages of all previous tokens. Hence, the CS assumption would be invalid? In addition, the theory would predict that fully sparse attention (e.g., entmax-based) would perform better, which contradicts empirical observations. Finally, what about recent recurrent models?
- Concerning CoT: can you clarify the points described above?
- "The work by Yau et al. (2024) bridges the gap from approximation to learning such with computations polynomially bounded histories." I do not understand this sentence.

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Questions
How do the works in the fields of compositional generalization, causal inference, and identifiability fit into your narrative?

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Questions
Given that the authors are discussing how to partition the input space and how to represent general functions/algorithms as DAGs, there should be citation and discussion of 

Smale's original work "On the Topology of Algorithms"

as well as Michael Shub's review paper "On the Work of Steve Smale on the Theory of Computation"

These works are essentially the foundation of modern Topological Complexity Theory, which, with the recent introduction of Topological Deep Learning, could be a fruitful interaction area for your suggested area of research.

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Questions
Please see the above weakness.

### Rating
4

### Confidence
4