Now I'll produce the final consolidated review.

## Summary

FedAIoT presents a federated learning benchmark for AIoT, curating eight datasets from authentic IoT devices (smartwatches, smartphones, Wi-Fi routers, drones, smart home sensors, AR headsets) and providing a unified end-to-end FL framework with non-IID partitioning, IoT-specific preprocessing, and IoT-factor emulation. The paper reports systematic benchmarking results on data heterogeneity, client sampling, noisy labels, and quantized training. The dataset curation is thoughtful and addresses a genuine gap, but the paper's impact is constrained by unverified claims and the absence of released code.

## Strengths

- **First FL benchmark built on data from authentic IoT devices with unique modalities.** Table 1 and Sections 3.1-3.2 show FedAIoT covers wireless CSI (UT-HAR, Widar), drone imagery (VisDrone), smart-home sensor streams (CASAS), and AR acoustics (EPIC-SOUNDS) — modalities that prior benchmarks like FLamby, FedAudio, FedCV, and FedNLP do not include. This is not merely argued; the paper identifies the gap in Related Work (ll. 89–94) and provides the curated datasets with evidence of use.

- **IoT-hardware-grounded experimental design.** Table 5 maps each dataset to specific representative devices with actual RAM ranges (Apple Watch 8: 512 MB–1 GB, TP-Link AX1800: 64 MB–1 GB, DJI Mavic 3 + Raspberry Pi 4: 1 GB–8 GB). This grounds the benchmark in real hardware constraints rather than abstract settings, and the quantized-training results (Table 7) are discussed relative to those concrete constraints.

- **Three distinct non-IID partitioning schemes adapted to task type.** Section 3.2.1 provides separate schemes — Dirichlet over output labels (classification), KNN-clustering on ImageNet features (object detection for VisDrone), quantile binning for output distribution (regression for AEP) — rather than a one-size-fits-all approach common in prior benchmarks. This demonstrates careful attention to data modality differences across IoT tasks.

- **First FL benchmark to incorporate client-side quantized training alongside server-side quantization.** The framework includes FP16 quantization on both sides, with measured memory reductions of 57%–63% across all eight datasets (Table 7). While the experiments have limitations (see Weaknesses), the distinction from FLUTE (server-side only) is genuine.

## Weaknesses

### Major

- **Code and preprocessed data not released.** Line 474 states the authors "aim to foster community collaboration by launching an open-source repository" — this is a future plan, not a current release. For a benchmark paper whose primary contribution is the benchmark itself (framework + curated data), the code, preprocessing scripts, and partition configurations must be usable by the community. Reproducing eight datasets from textual descriptions alone would be substantial work. This is the critical gap for a paper of this type and must be resolved for the contribution to stand.

- **Quantized training claims outpace the evidence.** The paper claims to be "the first FL benchmark to show the effect of quantized training on both server and client sides" (l. 80). However: (a) experiments only test FP16 (half-precision), not the low-bit quantization (INT4/INT8) most relevant for resource-constrained IoT. The paper acknowledges PyTorch does not support this (l. 417) but does not discuss whether quantization-aware training or alternative frameworks could fill the gap. (b) Memory usage is measured "under a centralized setting" on an NVIDIA A6000 GPU (l. 417), not on representative IoT hardware. The paper's justification (l. 418) that memory is "hardware-independent" partially addresses this, but the absolute numbers (e.g., 1444 MB for an LSTM on a smartwatch) do not directly inform whether a model fits on a device with 512 MB–1 GB total RAM, since GPU memory ≠ on-device RAM consumption. (c) The claim about "both sides" would be strengthened by ablating server-only vs. client-only quantization, which is not done.

### Minor

- **"Novel" noisy label design is overstated.** The paper claims a "novel way to design noisy labels" (l. 77) and a "new label transition probability matrix that breaks [the pairwise] assumption" (ll. 301). However, confusion-matrix-based transition matrices are standard in the label noise literature (Patrini et al., 2017, which the paper itself cites in l. 296). The paper's actual contribution — using this *in the FL benchmark context* where prior FL-specific works used pairwise or uniform noise — is legitimate, but the unqualified "novel" framing is imprecise. This should be scoped to novelty relative to prior FL benchmarks.

- **Client-to-real-device mapping is unclear.** For WISDM (45 training subjects, 80 clients per Table 1), the paper does not explain how 80 clients are derived from 45 subjects. Are clients subject-session pairs or entirely synthetic Dirichlet partitions? The partitioning section (3.2) describes the Dirichlet algorithm but does not clarify whether clients correspond to distinct IoT devices. This ambiguity weakens the realism claims of the benchmark.

- **Missing training hyperparameters limit reproducibility.** The paper does not specify learning rates, batch sizes, number of local epochs, or any optimizer-specific hyperparameters (momentum, weight decay, etc.) for the FL experiments. Total training rounds are listed (Table 3: 300–3000) but without rationale. This is an addressable gap but makes independent reproduction harder than necessary.

- **Statistical comparisons lack rigor.** Results are reported over three seeds with standard deviations, but comparative claims (e.g., "FedAvg has better performance than FedOPT" on WISDM/Widar datasets) are stated without statistical tests. With only three seeds and overlapping error bars in several cases (e.g., WISDM-P at α=0.1: FedAvg 34.28±3.28 vs FedOPT 32.99±0.55), some claimed differences may not be significant.

- **Insights are largely confirmatory.** The main benchmark observations (higher heterogeneity hurts performance, higher sampling ratio improves accuracy, noisy labels degrade accuracy, FP16 reduces memory) are well-established FL phenomena. The paper does provide dataset-specific granularity (identifying which datasets are more/less sensitive to each factor), but it does not include a comparison against non-IoT data to demonstrate *what is qualitatively distinct* about FL behavior on IoT modalities. This weakens the thesis that an IoT-specific benchmark surfaces uniquely different challenges.

### Trivial

- None beyond parser artifacts.

## Nice-to-Haves

- A direct comparison experiment between an IoT data modality and a standard non-IoT dataset of similar task complexity would sharpen the thesis that IoT data surfaces distinct FL challenges.
- Including benchmark results with personalized FL methods or noise-robust algorithms would increase utility as a community resource.
- A limitations section acknowledging the synthetic nature of Dirichlet-based non-IID partitions and the absence of realistic FL challenges (stragglers, device heterogeneity, communication costs) would improve completeness.

## Removed Points

The following points from the input reviews were removed after verification against the paper:

- **"Only two FL optimizers benchmarked"** (Harsh Critic): Two optimizers is standard coverage for a benchmark paper. The framework supports more; this is not a weakness.
- **"No noise-robust algorithms benchmarked"** (Harsh Critic): The paper documents problems via baselines. Benchmarking solutions is valuable future work but not required for a benchmark paper's core contribution.
- **"Does not separate server vs client quantization experimentally"** (Harsh Critic): The paper's claim is about including client-side quantization (contrasting with FLUTE which only does server-side). Applying FP16 on both sides is sufficient to support this claim; an ablation would strengthen but is not required.
- **"FedAudio/FLUTE may already cover IoT data"** (Harsh Critic): FedAudio covers generic microphone audio; FLUTE covers images and text. Neither is explicitly curated around IoT devices. The paper's comparison in Table 1 is reasonable.
- **"The claim that no existing benchmark covers IoT data would be more convincing if explained why data in those benchmarks does not qualify"** (Harsh Critic): The paper does explain (ll. 26, 89–94, Table 1) — existing benchmarks are designed around data modalities (CV, NLP, audio), not around IoT devices. This is sufficiently addressed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring tension between genuine contribution (IoT dataset curation, thoughtful framework design) and inflated claims, but do not add fundamentally new observations beyond what is on the page.

## Suggestions

1. **Release the code and preprocessing scripts** — the single most impactful action. Without this, the benchmark cannot be adopted or built upon.
2. **Qualify the novelty claims:** scope the noisy label contribution to *relative to prior FL benchmarks* (not absolute novelty for confusion-matrix methods) and clarify what specific evidence supports the "both sides" quantization claim.
3. **Report learning rates, batch sizes, local epochs, and a rationale for the varying training rounds** to enable exact reproduction.
4. **Clarify the client-to-device mapping** for each dataset, explaining how the number of clients relates to the number of subjects, sessions, or devices.
5. **Add a limitations section** acknowledging the scope boundaries (synthetic non-IID partitions, centralized GPU memory as proxy, absence of realistic device heterogeneity simulation).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>