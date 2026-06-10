## Summary

This paper proposes MLP-KAN, a Transformer-based architecture that replaces the standard MLP layer with a Mixture-of-Experts (MoE) module containing both MLP experts (for representation learning) and FasterKAN experts (for function learning). The authors evaluate on symbolic regression (30 Feynman equations) and image/text classification (CIFAR-10/100, mini-ImageNet, SST-2), reporting that MLP-KAN achieves competitive results. The core idea of combining expert types in an MoE is architecturally interesting, but the paper's presentation is undermined by factual errors in describing its own results, unspecified baselines that make the comparisons uninterpretable, and a significant gap between the claims made in the abstract/introduction and what the evidence actually supports.

## Strengths

- **MLP-KAN is either first or second on all 30 Feynman equations** (20 best, 10 second-best), with substantial improvements over MLP on most equations and competitive performance against KAN (Table result:1). This demonstrates that the mixed-expert MoE routing can successfully harness the function-approximation strengths of KAN-based experts.
- **Best result on SST-2 sentiment analysis** (Table rep:repre_table): MLP-KAN achieves 0.935 accuracy and 0.933 F1, outperforming both MLP (0.931/0.930) and KAN (0.925/0.925), showing the architecture works on text data as well as vision.
- **Ablations on expert count and top-k routing** (Tables experts, ex) provide practical guidance — e.g., 8 experts with top-k=2 is a good cost-performance sweet spot, and top-k=3 degrades performance, a non-trivial empirical finding.

## Weaknesses

### Fatal

- **Factual errors in the results description.** The paper's narrative paragraph (line 270) makes two statements that directly contradict the data in Table result:1:
  1. For equation I.12.5, the paper claims MLP-KAN "achieves a lower RMSE ($3.61 \times 10^{-3}$) than both KAN and MLP." The table shows KAN's RMSE is $2.93 \times 10^{-3}$ (bold=best), meaning KAN outperforms MLP-KAN here. **The statement is false.**
  2. For equation I.15.3t, the paper claims MLP-KAN "outperforms both KAN and MLP with an RMSE of $7.18 \times 10^{-2}$ compared to KAN's $3.69 \times 10^{-2}$." The table shows KAN's $3.69 \times 10^{-2}$ is *lower* (better). **The statement is false.**
  
  The paper additionally claims "Across almost all equations, \model consistently outperforms both KAN and MLP" — but KAN wins on 10 of 30 equations. These errors are not matters of interpretation; they are straightforward misreadings of the authors' own table. This undermines confidence in the entire experimental section.

### Major

- **Baseline architectures are not specified.** MLP-KAN replaces the MLP layer in a Transformer block (line 187), giving it multi-head self-attention, residual connections, layer normalization, and 8 MoE experts. But the paper never states what architectures the "MLP" and "KAN" baselines are — standalone networks? Also Transformer-based? The comparison is uninterpretable without this information. A Transformer with 8 experts vs. a standalone 2-layer MLP would be an apples-to-oranges comparison. No parameter counts or FLOPs are provided to calibrate.

- **Core claim of "unifying" representation and function learning is not tested.** The abstract says MLP-KAN "eliminate[s] the need for manual model selection." Yet the experiments train entirely separate models on separate datasets for separate task types. A single MLP-KAN model is never tested in a setting requiring both vision and symbolic regression simultaneously. The "unification" is purely architectural (two expert types in an MoE), not functional. The claimed user-facing benefit is simply not evaluated.

- **Overclaimed framing relative to the evidence.** The abstract claims "optimal performance" and "remarkable results." However, MLP-KAN is *second-best* on 3 out of 4 representation learning benchmarks (CIFAR-10: 0.920 vs. MLP's 0.922; CIFAR-100: 0.750 vs. 0.752; mini-ImageNet: 0.679 vs. 0.680). These margins are tiny, but plain MLP wins. On the Feynman equations, MLP-KAN wins 20 of 30 but KAN wins 10. The evidence shows a model that is competitive but not dominant — a perfectly fine contribution that does not need inflated claims.

- **FasterKAN/KAN mismatch unaddressed.** The function experts use FasterKAN (cited Athanasios2024, lines 99, 127–158), while the baseline is "KAN" (cited liu2024kan). These are different architectures. The paper never discusses whether this gives MLP-KAN an unfair advantage, whether FasterKAN is equivalent to KAN, or why this design choice was made. A comparison controlling for KAN variant is essential.

- **No statistical significance or error bars.** Every result appears to be a single run. Differences between methods are often tiny (e.g., 0.920 vs. 0.922 on CIFAR-10), making them uninterpretable without variance estimates.

- **Missing critical ablations.** The ablations only vary expert count and top-k. There is no ablation comparing all-MLP experts vs. all-KAN experts vs. mixed MLP/KAN experts, which is the core question. No routing analysis (what fraction of tokens go to MLP vs. KAN experts per task). No comparison to a standard MoE Transformer (all MLP experts) with matched parameter count.

### Minor

- **Feynman evaluation underspecified.** No information on samples per equation, training/test splits, input distribution, or preprocessing.
- **Related work is generic.** Section 2 reads as a broad survey of deep learning rather than positioning this paper against specific prior work on combining expert types or the KAN-vs-MLP debate.
- **Repeated sentence verbatim.** "The main challenge in our method is effectively integrating MLPs and KANs..." appears twice (line 19), reflecting sloppy editing.

### Trivial

- Figure 1 is labeled `\label{tab:fig1}` and cited as `Figure~\ref{tab:fig1}`, a LaTeX cross-reference error.

## Nice-to-Haves

- Routing visualization/analysis showing what fraction of tokens are dispatched to MLP vs. KAN experts on different task types.
- Multi-task experiment where a single MLP-KAN model handles both vision and symbolic regression to directly test the "unification" thesis.
- Comparison to standard MoE Transformers (e.g., Mixtral-style with all-MLP experts) to isolate the effect of mixed expert types.

## Removed Points

The following points from the inputs were filtered:

- **"No code or reproducibility details" (Harsh Critic)**: The paper provides training details (batch size, learning rate, GPUs). Requesting full training logs is a reproducibility nitpick that exceeds what is standard for a conference paper.
- **"LLM citation imprecision" (Harsh Critic)**: The criticism about citing GPT-4/Claude as representation learning examples is a framing preference, not an actual weakness of the paper's technical contribution.
- **"Scaling law α=4 presented without source" (Harsh Critic)**: The claim cites liu2024kan, which is the original KAN paper. This is adequately sourced.
- **Strength Finder's "systematic ablation on expert count" overemphasis**: While this ablation exists, it is straightforward (increasing experts improves performance with diminishing returns) and not particularly novel.
- **Strength Finder's claim of "17 of 30" (actually 20 of 30)**: The specific count was slightly off but the broader point stands; corrected in the strengths above.

## Novel Insights

The most genuinely interesting finding in the reviews is that the paper's results narrative contains factual errors (misreading its own Table 1 for equations I.12.5 and I.15.3t). This is not a matter of reviewer disagreement — it is verifiable from the paper. This, combined with the unspecified baselines, means that even the paper's own reported evidence cannot be taken at face value without clarification from the authors. The architectural idea (mixed MLP/KAN MoE experts) is plausible, but the paper as written does not meet the evidentiary standards required to support its claims.

## Suggestions

1. **Specify baselines clearly.** State whether MLP and KAN baselines are also Transformer-based, report parameter counts and FLOPs for all methods, and match compute budgets or explicitly acknowledge disparities.
2. **Correct the factual errors.** The statements about I.12.5 and I.15.3t in the results narrative must be fixed — they directly contradict the data in Table result:1.
3. **Tone down claims.** Replace "optimal performance" and "remarkable results" with language that matches the evidence (competitive, often second-best on vision, strongest on Feynman and SST-2).
4. **Add the missing ablation.** Compare all-MLP experts vs. all-KAN experts vs. mixed MLP+KAN experts to isolate whether mixing expert types is what drives performance.
5. **Address the FasterKAN/KAN mismatch.** Explain why FasterKAN is used for function experts and whether the KAN baseline also uses FasterKAN or a different variant.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>