## Summary
The paper proposes an adaptation recipe to convert pretrained autoregressive LMs (GPT-2 and LLaMA2-7B) into discrete diffusion language models (DiffuGPT, DiffuLLaMA) using attention mask annealing, a shift operation, and a time-embedding-free architecture, justified by showing AR cross-entropy is a special case of the absorbing discrete diffusion ELBO. The authors train models from 127M to 7B using <200B tokens and evaluate on a broad benchmark suite spanning commonsense reasoning, math (GSM8K w/ CoT), code/story infilling, and unconditional generation. The 7B DiffuLLaMA is, at submission, the largest released discrete diffusion LM.

## Strengths
- **Principled connection between AR and absorbing discrete diffusion objectives** (§3.2, Eq. 6–7): the paper derives that AR cross-entropy is recovered as a special case of the discrete diffusion loss up to a reweighting and indicator, giving theoretical grounding for AR→DLM adaptation.
- **Concrete, reproducible engineering recipe**: shift operation, attention-mask annealing, and removing time embedding are each ablated on GSM8K-symbolic at 127M/355M (Table 3/4), with DD aligning better with AR initialization than CD.
- **First 7B discrete diffusion LM released** with code, evaluation toolkit, and three scales — concrete artifact contribution to the community.
- **Broader evaluation surface than prior DLM work**: rather than perplexity-only (Plaid/SEDD norm), the paper evaluates commonsense MC, GSM8K with CoT, ICL/self-consistency, infilling, and unconditional generation perplexity vs. diversity (§4.2, Fig. 3). §4.3 makes a fair point that Plaid's low ppl does not transfer to conditional generation.
- **Inference latency advantage at long sequence lengths** is demonstrated empirically (Fig. 5: T=256 vs. LLaMA2 with KV-cache at 1024+ tokens).

## Weaknesses

### Fatal
None — the core artifacts and qualitative claims are supported by Table 1/2/3, even if some headline framings overshoot.

### Major
- **"Scaling" claim is not backed by a scaling-law experiment.** The title and §3.4 promise scaling, but the evidence is three loss curves on different data mixes at different token counts (Fig. 2 / §4.1), plus a 7B model that the authors themselves note "falls short of LLaMA2" on every task in Table 1 and attribute to insufficient training (§4.3). There is no compute-matched loss-vs-tokens plot across the three scales, so the central scaling claim is at best an existence/feasibility result, not an evidenced scaling trend. Compared to peer work that explicitly fits scaling laws (e.g., "Scaling up Masked Diffusion Models on Text"), this paper's framing outruns its evidence.
- **DiffuGPT vs. GPT-2 is confounded by ~30B extra FineWeb tokens.** The headline "DiffuGPT outperforms GPT-2" comparison in Table 1 does not include an AR continued-pretraining control on the same 30B FineWeb tokens. Table 3 contains a partial GPT-2 AR finetune number on GSM8K-symbolic only, where the gap is small/mixed. Without a matched-token AR continued-pretraining baseline across the Table 1 task suite, the gain cannot be cleanly attributed to the diffusion objective vs. additional data exposure.
- **Cross-class MC scoring is not commensurable.** §4.2 / §4.1 uses per-choice diffusion ELBO loss (Eq. 9) for DLMs and AR cross-entropy for AR baselines. The paper itself acknowledges (§4.2) that the diffusion loss is an upper bound on NLL and not directly comparable to AR NLL. Half of Table 1 (HellaSwag, Winogrande, SIQA, PIQA) rests on rankings of two non-commensurable losses; a single-sided importance-weighted bound or matched-mask AR scoring would be needed to make the comparison clean.

### Minor
- **Infilling comparison is acknowledged unfair, then still drives a headline claim.** §4.3 admits that AR baselines (GPT-2/LLaMA2) are not FIM-trained and receive only the prefix, "which might result in an unfair comparison," yet the abstract/§4.3 still concludes DLMs "demonstrate their strengths in infilling." A FIM-trained AR baseline (e.g., Code LLaMA or an FIM-finetuned LLaMA) on HumanEval-infill would substantially strengthen this. Per the rule that asymmetry-favoring-baselines is fine, the issue here is the opposite — asymmetry favors the proposed method — so this point stays.
- **Inference-speed Pareto for the 7B model is incomplete.** Fig. 5 reports latency at T=256 for 1024-token generation, but Fig. 3's quality-vs-T curves are for DiffuGPT, not DiffuLLaMA. A quality-vs-latency Pareto curve at 7B against LLaMA2 + KV cache is the natural claim and is missing.
- **Attention-mask annealing schedule is under-specified** (§3.3 "sample the amount of context from the right side and progressively increase" — no schedule given). Table 3 also reports that mask annealing has "minimal impact" and it is dropped entirely for the 7B run, which sits in tension with framing it as a core contribution in §1 and the conclusion.
- **Ablations are at 127M/355M only and extrapolated to 7B** without re-running at scale (the 7B drops mask annealing on the basis of small-scale ablation only).
- **CoT degrades performance (Table 2)** and is rationalized as "lack of instruction tuning"; an analysis of where the gap comes from would strengthen the §4.3 reasoning claim rather than deferring to future work.

### Trivial
- §3.4 / Fig. 2 caption presents loss curves on different data mixes and token counts as supporting a "scaling trend" — better axes/labels and at minimum compute-matched x-axes would help.

## Nice-to-Haves
- A compute-matched loss-vs-tokens scaling plot across 127M/355M/7B for AR→DLM adaptation.
- AR continued-pretraining control on matched 30B FineWeb tokens, evaluated across the full Table 1 suite.
- A FIM-trained AR baseline on HumanEval-infill and ROCStories.
- Quality-vs-T Pareto curve for DiffuLLaMA vs. LLaMA2 with KV-cache.
- Side-by-side generations from LLaMA2 and DiffuLLaMA with the same prefix at several T values, with quantitative quality metrics.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- "Unification of objectives is not novel (Austin 2021, Shi 2024)." — Removed: this criticizes prior-art coverage rather than correctness; the paper credits both works and uses the unification as motivation, not as the main claim. The contribution rests on the engineering recipe, which the paper itself acknowledges.
- Generic Strength Finder claims like "comprehensive evaluation beyond perplexity" and "time-embedding-free enables seamless weight transfer" — kept the first only because §4.2 has concrete substance; the latter is a design choice rather than a demonstrated benefit and is dropped.
- Strength: "Emergent in-context learning at 7B scale" — DiffuLLaMA's ICL numbers in Table 2 are weak in absolute terms and the gap-to-CoT is reported sympathetically (§4.3 explicitly calls out CoT degradation). Keeping it would conflict with the verified weakness about overclaimed reasoning, so it is moved here.

## Novel Insights
None beyond the paper's own contributions. The most interesting observation surfaced by the reviews — that DD-loss aligns naturally with AR initialization while CD does not (Table 3) — is the paper's own finding.

## Suggestions
- Reframe the title/abstract from "scaling" to "adapting" until a controlled scaling-law plot exists; the current artifact contribution is real but does not need the scaling-law framing to stand.
- Add the AR continued-pretraining control (Issue: Major #2) — this is the single experiment that would most strengthen the paper.
- Switch MC evaluation to a protocol that is commensurable across model classes (matched-mask scoring for AR or tighter NLL bound for DLM), and re-report Table 1.
- Add at least one FIM-trained AR baseline for infilling and either soften or strengthen the corresponding claim.

## Evaluation Axes
- **Originality**: Moderate — the AR↔DD ELBO equivalence is largely a restatement of Austin et al., 2021; the novelty is the adaptation recipe and the 7B-scale demonstration.
- **Importance of question**: High — adapting AR LLMs to DLMs is a practically important question for the diffusion-text community.
- **Claim support**: Partial — the artifact claims (we trained a 7B DLM with recipe X) hold; the comparative claims (DiffuGPT > GPT-2, competitive with AR counterparts, scaling) outrun the controls.
- **Soundness of experiments**: Mixed — broad task coverage but several confounds (token mismatch, non-commensurable losses, acknowledged-unfair infilling baseline).
- **Clarity**: Generally good; §3.3 mask-annealing schedule is under-specified.
- **Value to community**: High — released 7B DLM, code, and eval toolkit will be used regardless of whether every claim holds.

## Score and Decision

Anchors retrieved:
- `tyEyYT267x.md` — avg 8.00 — SAR (AR↔diffusion interpolation). Stronger novelty and cleaner methodology than this paper. Above ours.
- `Qn4HEhezKW.md` — avg 5.00 — "Diffusion LMs Can Perform Many Tasks with Scaling and Instruction-Finetuning." Nearly the same plan (adapt MLM/AR → DLM, scale, evaluate broadly), and got rejected at 5.00. Most direct comparator; this paper is somewhat stronger because of (a) the explicit AR↔DD ELBO derivation and (b) actually shipping a 7B model, but the empirical confounds are similar.
- `sL2F9YCMXf.md` — avg 6.75 — Energy-Based Diffusion LM. Cleaner methodological contribution; above ours.
- `WNvvwK0tut.md` — avg 6.50 — "Scaling up Masked Diffusion Models on Text." This is the natural high-band comparator: it actually fits a scaling law and reports CFG. Above ours on rigor; ours has a larger released model.
- `71mqtQdKB9.md` — avg 6.60 — SEDD. Strong methodology; above ours.
- `xI71dsS3o4.md` — avg 5.75 — survey on scaling-law fitting; tangential.
- `xGM5shdGJD.md` — avg 5.20 — scaling-law estimation guide; tangential.
- `iZeQBqJamf.md` — avg 6.50 — over-training scaling; tangential but high-band reference for rigor.
- `p6ncr0eTKE.md` — avg 6.50 — task-adaptive pretraining; tangentially relevant adaptation paper.
- `IhbZytsinc.md` — avg 6.00 — Minifinetuning; tangential.
- `i7oU4nfKEA.md` — avg 6.25 — multilingual LM; not closely related.
- `PtnttTKgQw.md` — avg 5.00 — mid-band general LM paper.
- `EJgxMsiAO9.md` — avg 5.20 — Alice in Wonderland; mid-band general LM.
- `QiyQJqpcYe.md` — avg 4.75 — Linguini benchmark; lower mid.
- `8QTpYC4smR.md` — avg 1.00 — survey paper; far below.
- `hCfhfwSfCg.md` — avg 2.00 — RL+LLM; far below.
- `NlY3XppPt3.md` — avg 2.00 — unsubstantive; far below.

This paper sits between Qn4HEhezKW (5.0, very similar in scope/framing, also rejected for unclear gains) and WNvvwK0tut (6.5, scaled-up MDM with proper scaling laws). The release of an actual 7B model and the broader eval push it above the 5.0 anchor; the missing matched-token AR control, the non-commensurable MC scoring, and the missing scaling-law plot keep it below the 6.5 anchor.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>