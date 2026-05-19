- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have all the information needed. Let me write the consolidated review.

## Summary
This paper attempts to prove theoretical limitations of Structured State Space Models (SSMs) for function composition and complex reasoning tasks, using communication-complexity lower bounds and log-space complexity characterizations. The paper proves that one-layer SSMs cannot efficiently perform function composition without large state sizes (Theorem 1), attempts to prove a Chain-of-Thought step lower bound (Theorem 2), and positions SSMs within complexity class **L** (Theorems 3 and 4). Experiments are described but results are not reported in the main paper.

## Strengths

- **Valid lower bound for one-layer SSMs on function composition (Theorem 1):** The paper provides a sound reduction from a communication-complexity lower bound (Lemma 1 from peng2024limitations) to show that an SSM with embedding dimension \(d\) and precision \(p\) solving function composition over domains of size \(n\) has error probability at least \(R/(3n\log n)\) when \((d^2+d)p < n\log n\). The proof correctly leverages the linear structure of the SSM recurrence to partition computation across agents (Grace computes the prefix, Faye computes aggregated matrix products over the suffix), and the communication count is correctly bounded. This constitutes a valid extension of the known Transformer bound to SSMs.

- **Clear connection of empirical tasks to complexity-theoretic problems:** The paper maps tasks like multi-digit multiplication, dynamic programming, and logical reasoning to well-studied computational problems (Circuit Evaluation, Derivability, 2-SAT, Horn SAT), grounding the empirical investigation in complexity theory. This framing is well-motivated and follows the established methodology of peng2024limitations.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 2 (CoT lower bound) proof is unsound — the protocol cannot be executed as described.** The proof (lines 179–180) states that in round \(r\), Alice computes \(\phi_{r, n+k}(\boldsymbol{x}_1, \dots, \boldsymbol{x}_{2n})\) — the \((n+k)\)-th hidden state of the SSM during the \(r\)-th CoT step — using only \(\phi_{r-1}\) and \(\boldsymbol{x}_1, \dots, \boldsymbol{x}_n\). However, the SSM recurrence \(\boldsymbol{h}_t = \boldsymbol{A}_t \boldsymbol{h}_{t-1} + \boldsymbol{B}_t \boldsymbol{x}_t\) depends on the input token \(\boldsymbol{x}_t\) at each step, and the matrices \(\boldsymbol{A}_t, \boldsymbol{B}_t\) themselves depend on \(\boldsymbol{x}_t\) (as stated in the definition, line 54: "the matrices \(\boldsymbol{A}_t = \boldsymbol{A}(\boldsymbol{x}_t)\), \(\boldsymbol{B}_t = \boldsymbol{B}(\boldsymbol{x}_t)\) are functions of the input vector \(\boldsymbol{x}_t\)"). The tokens \(\boldsymbol{x}_{n+1}, \dots, \boldsymbol{x}_{n+k}\) (which lie in the "Bob" portion of the prompt) are unknown to Alice. Without them, she cannot compute \(\boldsymbol{A}_{n+1}, \boldsymbol{B}_{n+1}, \dots, \boldsymbol{A}_{n+k}, \boldsymbol{B}_{n+k}\) nor the driving term \(\boldsymbol{B}_t \boldsymbol{x}_t\) for those positions. This is a genuine structural issue — the proof copies the Transformer CoT protocol from peng2024limitations, but SSMs lack the cross-position attention that would allow Alice to skip the intervening inputs. Since Theorem 2 is presented as a central contribution (the abstract calls it "a critical insight"), this flaw undermines one of the paper's main claimed results. The bound \(\Omega(\sqrt{n\log n}/(dp))\) is unsupported.

2. **No experimental results reported in the main paper.** The paper repeatedly claims empirical validation — the abstract states "Our experiments corroborate these theoretical findings" and "Evaluating models on tasks ... we find significant performance degradation" — yet Section 7 (Experiments, lines 254–262) contains only a setup description: model names (GPT-4, Jamba), hardware, and evaluation protocol (3 runs, 500 samples). No accuracy numbers, tables, figures, or error bars are presented. The only specific numbers in the paper (27% for GPT-4, 17% for Jamba on 4×3-digit multiplication) appear in the introduction (lines 16–17) as motivating examples, not as experimental results of this paper. The paper therefore provides zero empirical evidence for its empirical claims. A paper that frames empirical validation as integral to its contribution must present that evidence in a verifiable form.

3. **Theoretical novelty is limited.** The paper's contributions must be evaluated against prior work the authors themselves cite:
   - Theorem 1 adapts the communication-complexity proof from peng2024limitations (originally for Transformers) to SSMs, using the same Lemma 1 and a similar reduction. The adaptation is valid but closely follows the existing template, and the core proof technique (partitioning the function description across agents, computing aggregated matrix products) is inherited directly.
   - Theorem 3 (log-space computation of SSMs) is a re-derivation of a known result: the paper itself cites merrill2024illusion as already establishing that linear and S6-SSMs belong to logspace-uniform \(\mathbf{TC}^0 \subseteq \mathbf{L}\). The proof sketch (lines 207–240) is informal — it does not specify the machine model, does not argue that the functions computing \(\boldsymbol{A}_t, \boldsymbol{B}_t\) from input tokens are themselves logspace-computable, and does not address how the matrices are computed from \(\boldsymbol{x}_t\) in the general (input-dependent) case. This informal sketch does not constitute a rigorous new result.
   - Theorem 4 is a direct restatement of corollaries from merrill2024illusion and peng2024limitations, applying known NL-completeness/P-completeness results to SSMs given their membership in \(\mathbf{TC}^0\).

   The one genuinely novel theoretical claim was the CoT bound, and that proof is flawed (point 1 above).

### Minor

- **Theorem 3 proof is too informal for a complexity-theory paper.** Even setting aside novelty, the proof does not define the machine model, does not argue that the functions computing \(\boldsymbol{A}_t, \boldsymbol{B}_t, \boldsymbol{C}_t, \boldsymbol{D}_t\) from \(\boldsymbol{x}_t\) are logspace-computable (they are arbitrary functions of the input in the general SSM definition), and does not address how to handle the input-dependent matrices. The claim that "each element of these matrices can be represented using \(O(\log N)\) bits" is necessary but not sufficient — one must also show how to compute them within the logspace bound.

- **No quantitative bridge between theory and experiments (even hypothetically).** The paper makes no attempt to instantiate the bounds from Theorems 1 and 2 (which involve \(n, d, p\)) for the specific tasks evaluated. For example, one could project what domain size \(n\) would be required to make the theoretical bounds non-vacuous for the model dimensions used. The absence of such a bridge, combined with the missing experimental results, makes the theory–experiment connection purely rhetorical.

### Trivial
None.

## Nice-to-Haves
- If the CoT proof can be repaired, the paper would benefit from discussing why the Transformer proof technique does not transfer directly to SSMs and what new obstacles the sequential recurrence introduces.
- The log-space proof could be strengthened by specifying a concrete logspace Turing machine or LOGSPACE-uniform circuit family, and by addressing input-dependent matrix computation.

## Removed Points
- **Criticism about Theorem 1 being "the same reduction":** While Theorem 1 adapts a known proof template, this is a standard and acceptable practice — extending bounds to a different architecture. The reviewer's characterization as "essentially copying" is overly dismissive of a valid adaptation that required verifying the SSM recurrence supports the communication protocol.
- **Criticism that the SSM-Equivalence section "does not add novelty":** This section is background/context, not a claimed contribution. It situates the work.
- **Criticism about Theorem 3 proof being "too informal":** This is moved to Minor (it is a real concern but less severe, as the result itself is already known).
- **Strength Finder's claim of "concrete accuracy numbers" in experiments (Supporting Strength 1):** The 27%/17% numbers are in the introduction as motivation, not in the experiments section. The experiments section itself contains zero reported results. This strength is misleading and is removed.
- **Strength Finder's claim about "log-space characterization" (Core Strength 3):** Downgraded; the result is known and the proof sketch is informal. The strength is partially valid but significantly overwrought in the Strength Finder.
- **Strength Finder's claim about "Connecting SSMs to known complexity-class barriers" (Supporting Strength 2):** This is a straightforward application of the cited prior work (merrill2024illusion, peng2024limitations). It adds no new insight beyond recitation.
- **Criticisms about reproducibility (trivial implementation details):** Removed per filtering rules.
- **Criticism about missing related work:** Removed — I cannot verify what other work exists.
- **Formatting/presentation nitpicks:** Removed per filtering rules.

## Novel Insights
The harsh critic's observation about the CoT proof flaw — that the SSM's sequential recurrence prevents Alice from computing the hidden state at position \(n+k\) without knowing the intervening inputs — is a genuine and insightful critique that identifies a non-trivial gap between SSMs and Transformers. The attempted proof copied the Transformer protocol, but the Transformer's ability to attend across arbitrary positions would have allowed Alice's computation; the SSM's strict sequentiality (and input-dependent matrices) does not. This highlights that extending lower bounds from Transformers to SSMs is not always straightforward, and the structural differences between attention-based and recurrence-based architectures matter for communication-complexity reductions. None beyond the paper's own contributions.

## Suggestions
1. **Fix or remove Theorem 2.** If the CoT lower bound is true, a different communication protocol is needed — one that accounts for the fact that Alice cannot see intermediate input tokens during the SSM forward pass. One possible approach: have Bob send the aggregated matrix product (as in Theorem 1's protocol) for the Bob-known segment, and have Alice combine it with her prefix computation. However, the multi-round nature of CoT makes this non-trivial. If a correct proof cannot be found, the claim should be removed or downgraded to a conjecture.

2. **Restore experimental results or adjust claims.** The paper must present the actual results (accuracy tables, error bars, comparisons) for the experiments described in Section 7. If the experiments section was stripped by the PDF parser from the appendix but exists in the full submission, a summary of key results must be included in the main text for the paper to be evaluable. The abstract and conclusion should be adjusted to reflect the actual evidence presented.

3. **Strengthen the log-space proof or cite the prior result directly.** The informal proof sketch should either be made rigorous (specifying the machine model, addressing input-dependent matrix computation) or the paper should simply cite merrill2024illusion for the \(\mathbf{TC}^0\) membership and note that this implies \(\mathbf{L}\) membership.
