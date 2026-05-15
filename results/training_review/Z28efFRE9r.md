Now I have a thorough understanding of the paper. Let me construct the consolidated final review.

---

## Summary

AuthFace proposes a two-stage pipeline for blind face restoration (BFR). Stage I fine-tunes StableDiffusion-XL (SDXL) on a curated 1.5K dataset of ultra-high-resolution (8K+) professional face photographs annotated with photography-guided captions, producing a face-oriented generative prior. Stage II trains a ControlNet with a time-aware latent facial feature loss that weights intermediate diffusion steps to constrain eyes and mouth regions. The method achieves state-of-the-art results on most no-reference quality metrics (MANIQA, MUSIQ, CLIPIQA) across multiple synthetic and real-world benchmarks, with compelling qualitative improvements in skin texture, eyelashes, and teeth.

## Strengths

- **Consistent SOTA on no-reference metrics across multiple datasets.** In Table 1, AuthFace achieves the highest MANIQA, MUSIQ, and CLIPIQA on CelebA-Test, LFW-Test, WebPhoto-Test, and WIDER-Test, often by substantial margins (e.g., MANIQA 0.6431 vs. 0.5528 on LFW-Test). This consistency across four datasets with different degradation profiles demonstrates robustness.

- **Photography-guided annotation is a thoughtful adaptation for face-oriented fine-tuning.** The paper identifies that semantic-only captions miss stylistic cues (lighting, skin texture, makeup) critical for face restoration, and uses LLaVA-1.6 with photography-guided prompts to capture this information. The approach moves beyond generic captioning strategies used in prior fine-tuning pipelines (Emu, CosmicMan).

- **Time-aware latent facial feature loss is a well-motivated novelty.** The ablation (Table 2, experiments c vs. d) confirms that weighting the facial loss by diffusion timestep — focusing on intermediate steps where eye/mouth shapes emerge — improves over a constant-weight baseline on all no-reference metrics (MANIQA 0.6449→0.6624, MUSIQ 73.66→75.76 on CelebA-Test). Figure 6 qualitatively demonstrates reduced artifacts.

- **Compelling qualitative results on challenging cases.** The paper shows restoration of side faces, teeth, glasses edges, and skin texture where multiple baselines (GFP-GAN, CodeFormer, SUPIR) fail, as shown in Figures 4–6. The improvements in fine facial details are visually clear and non-trivial.

## Weaknesses

### Fatal
None.

### Major

- **Poor FID scores directly challenge the "authentic" framing.** On CelebA-Test, AuthFace achieves FID 50.93 — substantially worse than SUPIR (35.01) and BFRffusion (40.74). On LFW-Test and WebPhoto-Test, AuthFace also underperforms SUPIR on FID. F