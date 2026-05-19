- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8
Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper introduces a complete pipeline for the de novo generation of endoskeletal robots — soft-bodied agents with jointed internal skeletons. It combines (i) a novel massively-parallel voxel-based multi-physics simulator supporting two-way coupling between deformable soft tissues and rigid bones with joint constraints, (ii) a deep VAE trained on procedurally generated endoskeletal designs to produce a smooth, continuous latent embedding, (iii) a universal graph-transformer policy that co-adapts with morphology via local pooling of mechanosensory data, and (iv) CMA-ES for morphological evolution in the latent space. The system produces diverse, qualitatively convincing body plans across four terrestrial environments (flat ground, upright locomotion, potholes, mountain), and control experiments demonstrate that cumulative morphological evolution is necessary for achieving high fitness.

---

## Strengths

1. **A genuinely novel and complete system for endoskeletal robot design.** The paper is the first to bridge fully rigid and fully soft robot design by co-optimizing both external soft tissues and internal jointed skeletons in a single pipeline (Sect. 2). The combination of simulator, learned latent representation, graph-transformer-based universal controller, and evolutionary optimization constitutes a coherent, non-trivial technical contribution that goes beyond prior work targeting either extreme in isolation.

2. **Well-designed control experiments isolating the effect of morphological evolution.** The paper does not merely show that the pipeline works — it systematically demonstrates that evolution on the latent manifold produces substantially better body plans than random search (Fig. 6A,B), and that designs from evolved populations, when frozen and re-trained from scratch, dramatically outperform frozen initial designs (Fig. 6C). This directly supports the claim that cumulative selection in latent space is essential.

3. **A smooth, expressive latent embedding with interpretable structure.** The VAE latent space is shown to support smooth linear interpolation (Fig. 4), correlates with interpretable morphological traits (body height, length, bone count — Figs. 14–16 in appendix), and generalizes beyond the training distribution by producing features such as skeletal voids not present in the synthetic training data (Sect. 3.1). This provides a principled genotype-phenotype mapping for evolution.

4. **Demonstrated diversity of evolved morphologies across task environments.** Across four distinct terrains, the system produces qualitatively different body plans — snakes for flat ground, legged walkers with upright reward, foot-like appendages for potholes — showing that the method can discover task-appropriate designs without hand-engineering (Sect. 3.2, Fig. 5).

5. **Benchmarking infrastructure released.** The paper states that the simulator, four task environments, and an object manipulation example are provided as a platform for future work (Sect. 4), which will be valuable to the community.

---

## Weaknesses

### Fatal

None. The core claims are supported by the system as presented. The paper delivers on its promise of a working end-to-end pipeline for generating endoskeletal robots.

### Major

1. **No quantitative comparison to prior design methods.** The paper positions itself as bridging fully rigid and fully soft robots, and the introduction explicitly critiques limitations of prior work (CPPN-evolved soft voxels, graph-grammar rigid bodies, stick-figure controllers). Yet the results provide no direct comparison — quantitative or qualitative — to any existing method on the same tasks. A reader cannot assess whether the endoskeletal approach actually improves over simpler alternatives (e.g., a pure-soft body evolved with CPPNs, or a rigid chain with joints). This is the most significant gap: the paper's central narrative of "going beyond" prior work is asserted rather than demonstrated through comparison. This matters because without baselines, the value added by the substantial complexity of the pipeline is unclear.

2. **Only two independent evolutionary trials are reported, with limited statistical characterization.** The paper states "two independent evolutionary trials were conducted" per environment (Fig. 5 caption) and shows only one best design and one cumulative-max curve per environment. Fig. 6A does include 95% bootstrapped confidence intervals for the upright locomotion environment, but variance across trials for the other three environments is not reported. For a paper making claims about the reliability and general effectiveness of the approach, more trials and better characterization of variance are expected.

### Minor

3. **VAE reconstruction quality is asserted but not quantitatively measured.** The paper states that the VAE encodes and decodes designs with "high accuracy" (Sect. 3.1, referencing Fig. synth_vs_decode) and shows qualitative interpolations, but provides no quantitative reconstruction metric (e.g., mean IoU, voxel-wise accuracy, or FID) on held-out synthetic data. This makes it difficult to assess how reliably the decoder maps arbitrary latent points to physically valid, mechanically connected robots, which is important since the VAE serves as the genotype-phenotype mapping for evolution.

4. **The simulator, though a core contribution, is not validated against known cases.** A new multi-physics simulator is introduced and all experimental results depend on its fidelity. While the simulator builds on established physics (Euler-Bernoulli beams, Newtonian mechanics, constraint-based rigid body dynamics), no validation against a simpler known case (e.g., a rigid pendulum, a soft block under gravity, a jointed chain) is presented. This concern is partly mitigated by the paper's honest admission that the most important limitation is the lack of physical realization, and by the community standard of accepting simulation-only results in this field — but given the centrality of the simulator to all claims, some basic sanity-check validation would substantially strengthen reader confidence.

5. **The random search baseline in the necessity-of-evolution experiment is not fully specified.** Random morphological search is compared to CMA-ES (Fig. 6A,B, purple curves) and shown to perform worse, but the text does not describe how many random designs were evaluated per generation-equivalent or whether the computational budget was matched. This limits the strength of the conclusion that "evolution is necessary."

6. **Limited ablation of pipeline components.** The pipeline has many interacting components (VAE, graph-transformer policy, spatial pooling, reward function, CMA-ES, filtering heuristics). While the paper does include meaningful ablations (discrete vs. continuous actions, evolution vs. random search), it does not isolate the contribution of each component — e.g., whether a simpler representation (direct parameterization of bones/joints, bypassing the VAE) would work as well, or how sensitive results are to latent dimension, reward shaping parameters, or the upright-reward threshold (5 cm). This makes it hard to know which design choices are critical.

### Trivial

None of note.

---

## Nice-to-Haves

- A single direct comparison — for example, on flat ground, comparing an evolved endoskeletal snake to a pure-rigid chain with the same number of joints, or to a pure-soft body without skeleton, using the same RL training pipeline — would directly test the claim that endoskeletal design confers an advantage.
- Reporting multiple random seeds (≥5) for each environment would substantially strengthen statistical reliability.
- A brief quantitative characterization of VAE reconstruction performance (e.g., mean IoU between decoded designs and their encoded originals) would help readers gauge representation quality.
- A failure-mode analysis (e.g., when does the VAE produce invalid designs? when does evolution get stuck?) would enrich the discussion.

---

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper. They should be treated with caution.

1. **"Fewer than 15% invalid designs is surprisingly high"** — This is a misreading. The paper reports that fewer than 15% of randomly generated designs were **invalid** (fewer than 2 joints or <20% bone), meaning 85%+ were valid. This is favorable, not problematic. **Removed: factually wrong.**

2. **"Architecture details missing from main text (VAE depth, hyperparameters, learning rates)"** — The paper explicitly refers to appendix sections (Appx. appx:more_hypers, Appx. appx:synth_data_gen) for these details. The parser strips appendices; they exist in the original submission. **Removed: appendix content, not author error.**

3. **"Simulator key details deferred to appendix"** — Same rationale as above. The paper provides the central dynamical equation (Eq. 1) and references the appendix for extended detail, which is standard practice. **Removed: appendix content.**

4. **"Discrete action space justification references a figure not in the main text"** — The paper references Fig. fig:discrete_vs_continous. Whether this figure appears in the main text or appendix is a formatting matter. **Removed: formatting nitpick.**

5. **"Paper does not discuss how simulation inaccuracies could affect conclusions"** — The Discussion (Sect. 4) explicitly states that the lack of physical realization is the "most important limitation" of the paper, which directly encompasses this concern. **Removed: already addressed by the authors.**

6. **"The introduction sets up expectations the results never deliver"** — This is a framing of the missing-baselines criticism (already kept as Major weakness #1). As a standalone point it is too vague. **Merged into Major weakness #1.**

7. **"Missing related works"** — Per guidelines, I cannot verify the existence of missing references. **Removed: cannot verify.**

---

## Novel Insights

The reviews offer two observations that go beyond what the paper itself explicitly states. First, the paper's design is notable for the *principled way* it leverages unlimited synthetic data to train a deeper voxel-based autoencoder than prior work — an insight that could be applied to other domains where data is scarce but can be procedurally generated. Second, the combination of local pooling (aligning voxel-level mechanosensory data to the skeletal graph) with a graph transformer is an elegant architectural solution to the variable-topology control problem that deserves attention from the broader multi-agent or embodied-AI community as a general pattern. Neither observation is entirely absent from the paper, but the reviews help crystallize them as contributions that go beyond "yet another evolutionary robotics system."

---

## Suggestions

1. **Add at least one quantitative baseline comparison.** Even a single environment (flat ground) comparing endoskeletal robots to a pure-rigid chain or a pure-soft body using the same RL pipeline would significantly strengthen the paper's core claim about bridging the two extremes.
2. **Report quantitative VAE reconstruction metrics** (e.g., mean IoU, structural similarity) on held-out synthetic data, and characterize the rate at which random latent codes decode to valid (mechanically connected, non-self-intersecting) designs.
3. **Run more independent trials** (at least 5) for each environment and report variance alongside the cumulative-max plots.
4. **Validate the simulator** against a simple known case (e.g., a pendulum, a dropped block, a cantilever beam) using an analytical solution or a reference physics engine, even briefly, in the main text or appendix.
5. **Ablate the VAE** by comparing CMA-ES on the latent space to CMA-ES directly on a simpler parameterization (e.g., bone count, joint angles, bone lengths), to isolate the contribution of learned representation.

---
