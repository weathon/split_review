- Decision: Accept
- Scores: 5, 5, 8, 3

## Merged Review

### Summary
The paper analyzes Multigrid Parametric Encodings (MPE) through the Neural Tangent Kernel (NTK), showing that MPE raises the eigenvalue spectrum compared to coordinate-based MLPs and outperforms Fourier Feature Encodings (FFE) on 2D image regression (ImageNet, 100 synonym sets) and 3D implicit surface regression (Stanford graphics dataset). The theory isolates that MPE’s improvement stems from grid structure, not the learnable embedding. Reviewer 3 notes a clear theoretical contribution backed by solid experiments; Reviewer 4 questions the take‑away, finds examples cherry‑picked, and criticizes the lack of discussion on grid choice. Reviewer 2 finds limited novelty and evaluation, while Reviewer 1 praises the NTK analysis approach.

### Strengths
- **NTK framework to analyze encoding schemes**: Using the NTK spectrum to compare MPE and FFE makes the theory concise (R1, R3).
- **MPE practical effectiveness**: MPE significantly outperforms baseline and FFE on image and surface regression, with up to 15 dB PSNR / 0.65 MS‑SSIM over baseline (R1, R2, R3).
- **Theory isolates grid structure vs. embedding**: Proving that the grid structure, not the learnable embedding, drives performance fills an important gap (R2, R3).
- **Clear exposition**: The paper redefines terms, provides clear examples and expressions for the tools used (R3).
- **Well‑structured and to the point**: Theoretical contribution is directly supported by experiments (R2, R3).
- **Subsequent empirical validation**: Theoretical claims are validated on ImageNet images and 3D surfaces (R4).
- **Straightforward improvement over baseline**: MPE yields an 8‑order eigenvalue increase over baseline (R4).

### Weaknesses
- **Writing clarity and notation**:  
  - Equation (1): dimension of \(x\) and \(\gamma_F(x)\) unclear (R1).  
  - Equation (3): “round +” notation not defined (R1).  
  - Equation (7): size of \(Q\) vs. \(y\) dimension unclear (R1).  
  - Equation (9): missing expectation for NTK definition, derivative without specifying which parameter (R1, R2).  
  - Theorem 1: statement is unclear; \(\lambda_i^{MPE}\) and training set size need clarification (R1).  
  - Figures: “Identity” in plots not explained (R4); Fig. 1 input dimension (\(d=2\) or 3) confusing (R3).  
  - Notation: \(f_\theta(x)\) and \(\gamma(x)\) use same \(x\); limitation \(d \le 3\) not discussed (R3).  
  - Baseline network not defined (R4).
- **Conceptual link**: It is unclear how the NTK eigenvalue spectrum directly relates to high‑frequency information (large Fourier modes) (R1).
- **Limited novelty**: The work uses well‑known methods (NTK, MPE, FFE) and mostly re‑states existing theory (R2). The contribution is incremental rather than a new technique.
- **Insufficient evaluation**:  
  - Only ImageNet used for 2D regression; broader datasets needed (R2).  
  - Reviewer 4 finds examples cherry‑picked; asks for average eigenvalue spectrum across many runs/datasets (R4).  
  - Larger‑scale experiments (e.g., NeRFs, SotA models) would make the work more impactful (R3, R2).
- **Single‑layer MLP analysis**: The NTK derivation assumes a single‑layer network; extension to deeper networks is not provided (even in appendix), but deeper layers significantly affect NTK behavior (R2).
- **PSNR metric concerns**: PSNR (MSE‑based) is not sensitive to fine details; the paper does report MS‑SSIM but does not highlight it as a primary metric or use HFEN (R3).
- **Memory overhead**: The practical cost of MPE’s grid structure (especially at high resolution) is not discussed (R3).
- **Grid choice under‑examined**: The paper does not discuss alternatives such as irregular grids (e.g., fast multipole method) or partially learnable grids. The stability of regular grids is questionable; claiming the grid must be learnable is not convincingly justified (R4).
- **Missing comparisons**: Figure 2 omits the FFE eigenvalue spectrum, making the improvement over FFE unclear from the spectrum alone (R4). No comparison to classical image compression algorithms (R4).
- **Take‑away ambiguous**: It is unclear whether MPE always outperforms FFE, and under what conditions each encoding is preferable (R4).