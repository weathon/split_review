## Summary
This paper studies "measure-first" vs "fully-quantum" protocols in quantum machine learning, proving an exponential separation: there exists a measurement-learning task (based on the Hidden Matching problem) solvable by a fully-quantum protocol with polynomial resources, but requiring exponential resources for any measure-first protocol that must pre-measure input states via a data-independent measurement strategy. The paper extends prior worst-case results to average-case hardness and, using quantum-secure pseudorandom functions (QPRFs), shows the separation persists even when restricting to efficiently preparable (physically realizable) quantum states.

## Strengths
- **Average-case hardness, not just worst-case**: Theorem 2 quantifies explicit thresholds ($(1-\epsilon)(1-\delta) > 7/8$) for which the concept class is not measure-first learnable, improving on prior work (Grier et al. 2022; Bar-Yossef et al. 2004) that only established worst-case limitations. This matches the relevant standard in machine learning.
- **Separation with efficiently preparable states**: Theorem 3 extends the hardness result to phase states of QPRFs, which are efficiently preparable. This directly addresses the key limitation of earlier work that relied on unphysical states, using a clean distinguisher argument that reduces to the QPRF security guarantee (Definition 8).
- **Rigorous formal framework**: Definitions 3–6 provide a precise formalization distinguishing fully-quantum from measure-first protocols, with the key constraint (measurement strategy $M$ independent of the specific target concept) clearly stated.
- **Clean proof technique for the efficiently-preparable case**: The distinguisher argument (Section 3.3.2) elegantly shows that if a measure-first protocol worked on pseudorandom states, it would create a QPRF distinguisher, reducing the problem to a cryptographic hardness assumption rather than requiring structural assumptions about efficient quantum circuits.

## Weaknesses
### Fatal
None.

### Major
None.

### Minor
- **The fully-quantum upper bound is trivially successful, limiting conceptual depth**: Proposition 1's protocol simply reads $x$ from a training label and constructs a known circuit $U_x$ from Aaronson et al. (2023). The paper acknowledges this ("it might seem that little genuine learning occurs") and gestures at "partial information" variants, but never develops them. While this does not invalidate the separation (both protocols receive $x$ from labels—see Def. 3 Eq. 4 and Def. 5 Eq. 6—so the asymmetry is not about access to $x$), it makes the fully-quantum side of the separation conceptually shallow, and the claimed "learning" framing feels somewhat overstated.
- **High-level proof sketches**: The proofs of Theorems 2 and 3 are sketched in roughly 15 lines each. The core reductions (Yao's principle for Theorem 2; the distinguisher construction for Theorem 3) are described at a level where a reader cannot fully verify logical soundness without reconstructing substantial details. While conference length constraints may justify deferring details, the main text should give a more complete argument skeleton.
- **The measure-first definition is restrictive**: The measurement strategy $M$ cannot depend on the training data in any way—not even adaptively based on a subset of examples. This precludes natural hybrid strategies (e.g., use a small holdout set to decide measurements). The paper is transparent about this constraint, but the gap between the definition and practical quantum ML pipelines is not discussed, and it is unclear whether the separation would hold for adaptive variants.

### Trivial
- **Forward reference**: Definition 3 (line 101) references "the concept class $\mathcal{C}$ in Definition 7" before Definition 7 is introduced (line 162).
- **Unnecessary polynomial-time restriction**: Definition 5 requires $A$ to be polynomial-time, but the lower bound is information-theoretic (as the paper itself notes at line 195) and holds regardless. This is a minor imprecision in the definition.

## Nice-to-Haves
- Discuss whether the separation extends to adaptive measurement strategies (where $M$ can be updated based on a small subset of training data).
- Develop the "partial information about $x$" variants mentioned at line 182, which would significantly strengthen the conceptual contribution.
- Provide a concrete lower bound on the number of classical bits required (beyond "exponential").

## Removed Points
These points from the reviews were removed with brief justification:
- **Critic's "fatal" issue #1 (fully-quantum protocol "handed the answer" vs measure-first not)**: Factually incorrect. Both the fully-quantum protocol (Def. 3, Eq. 4) and the measure-first protocol (Def. 5, Eq. 6) receive $x$ in their training labels $(x,y,b)$. The separation arises from whether the quantum state survives to be processed, not from asymmetric access to $x$.
- **Critic's "fatal" issue #3 (communication-compression vs learning framing)**: The paper's conclusion explicitly acknowledges the anti-Holevo analogy. The result is a legitimate learning separation: both protocols face the same task; one solves it and the other cannot because quantum information cannot be compressed to $O(\text{poly}(n))$ classical bits. This is substantive even if the fully-quantum protocol is simple.
- **"Realistic" overstatement claim**: The paper uses "realistic" to mean "efficiently preparable" (not "naturally occurring"), standard in the field. No overstatement.
- **Strength Finder's "robustness to experimental imperfections"**: Claimed as a strength but not demonstrated in the accessible text. Since the weakness about absent justification wins per filtering rules, this strength is dropped.
- **Error-robustness criticism**: The footnote at line 143 is a parser artifact; the original submission likely contained a proper justification. Removed per parser-artifact filtering rule.
- **Missing related works / unverifiable references**: All cited works are assumed to exist per review instructions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Provide more detailed proof sketches for Theorems 2 and 3 in the main text, or at minimum a structured outline of the reduction steps and how Yao's principle is applied.
- Discuss whether the separation holds for adaptive measurement strategies and qualify the scope of the measure-first definition more carefully.
- Either develop the "partial information" variant or more carefully temper the framing of the fully-quantum protocol's "learning" to match its trivial nature.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>