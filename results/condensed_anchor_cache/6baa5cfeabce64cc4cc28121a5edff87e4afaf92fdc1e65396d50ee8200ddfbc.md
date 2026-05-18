- Decision: Accept
- Scores: 6, 8, 6

## Merged Review

### Summary
This paper challenges the prevailing view that Diffusion Posterior Sampling (DPS) works by approximating conditional score, hypothesizing instead that DPS is closer to maximizing a posterior (MAP). Through empirical analysis on 512×512 ImageNet images, the authors demonstrate that DPS’s conditional score estimation diverges from an accurate conditional model, exhibits a high mean deviation from zero, and produces low-diversity samples. Based on this reinterpretation, they propose two improvements: explicitly maximizing the posterior via multi-step gradient ascent and projection (DMAP), and incorporating a lightweight conditional score estimator trained on only 100 images and 8 GPU hours. The methods are shown to outperform standard DPS, especially in deblurring. One reviewer (rating 8) was notably more positive, praising the compelling evidence and significant improvements, while the other two (ratings 6) raised concerns about empirical reliance, missing experiments, and presentation issues.

### Strengths
- The paper is well-organized and provides clear explanations of technical details, including mathematical formulations and algorithms.
- The MAP hypothesis is a clear and novel contribution that can explain recent mysterious observations regarding DPS (e.g., why Adam helps, low diversity).
- Building on the reinterpretation, the proposed improvements (DMAP and the lightweight conditional score estimator) significantly enhance DPS’s performance, well supporting the hypothesis.
- The paper presents compelling empirical evidence on 512×512 ImageNet images that DPS does not effectively approximate the conditional score, contradicting prior understanding.
- The work has potential for significant impact as it introduces new ideas and reinterprets existing arguments in a popular field.

### Weaknesses
- The paper relies heavily on empirical observations to develop and support its claims; theoretical insights would strengthen the argument and more naturally lead to the MAP hypothesis.
- The work shows that the MAP hypothesis can explain the “weird” aspects of DPS but does not clarify why DPS works as a MAP estimator in the first place.
- The analysis is limited to image restoration tasks (mainly deblurring); generalizability to other inverse problems (e.g., inpainting, CT/MRI reconstruction, depth estimation) is not explored. The paper lacks results for inpainting, unlike the original DPS paper (one reviewer questioned: “Is DPS not used for inpainting as well? You seem to only provide results for deblurring.”).
- The lightweight conditional score estimator still lags behind well-trained conditional diffusion models like StableSR. The paper does not provide a detailed analysis of trade-offs between computational efficiency and performance, nor does it explore sensitivity to training sample size or conditional distribution complexity. (One reviewer suggested investigating whether the gap can be reduced with more sophisticated training or architectures.)
- The claim that the MAP hypothesis can explain why Adam helps DPS is not sufficiently substantiated; a rigorous analysis of how Adam’s specific update rules interact with DPS’s objective is missing (e.g., convergence analysis or comparison with other optimizers).
- The conclusion that “DPS is far away from a reasonable conditional score estimator in practical scenarios” is considered extreme, given it is based on evidence from only one problem (512×512 ImageNet deblurring).
- For a multi-modal posterior, is it valid to say that working as MAP is the main reason for low-diversity generation? (Reviewer’s question, reflects a limitation in explanation.)
- To further test the MAP hypothesis, experimenting with toy distributions where the ground truth posterior is known is suggested but not done.
- The paper contains several grammatical and presentation flaws: table captions should be on top (per ICLR formatting); add arrows to indicate metric direction (e.g., lower FID is better); many undefined acronyms (FID, KID, LPIPS); figure/table captions could be clearer by including the key takeaway as in the text; redundant math notation (line 196 vs line 153); typo “hypothesis” instead of “hypothesize” (line 255); misplaced appendix citation after a sentence (line 273); incorrect quotation marks (should use `` for opening); citation style errors (e.g., “Chung et al. (2022a); Song et al. (2023c)”).
- Despite presenting a reinterpretation and improvements, the work remains limited in scope: no results for inpainting and no theoretical justification for the MAP hypothesis beyond empirical observations.