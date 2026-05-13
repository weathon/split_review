# Sorting Out Quantum Monte Carlo

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Molecular modeling at the quantum level requires choosing a parameterization of the wavefunction that both respects the required particle symmetries, and is scalable to systems of many particles.
For the simulation of fermions, valid parameterizations must be antisymmetric with respect to the exchange of particles. 
Typically, antisymmetry is enforced by leveraging the anti-symmetry of determinants with respect to the exchange of matrix rows, but this involves computing a full determinant each time the wavefunction is evaluated.
Instead, we introduce a new antisymmetrization layer derived from sorting, the \emph{sortlet}, which scales as $O(N \log N)$ with regards to the number of particles -- in contrast to $O(N^3)$ for the determinant.
We show numerically that applying this anti-symmeterization layer on top of an attention based neural-network backbone yields a flexible wavefunction parameterization capable of reaching chemical accuracy when approximating the ground state of first-row atoms and small molecules.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a method based on sorting operations to achieve the anti-symmetry property of the NN-VMC ansatz. Compared with the original determinant ansatz, the proposed algorithm has a favorable computational complexity. The authors conduct experiments on small molecule systems, showing the proposed ansatz has a comparable performance as the baseline methods.

### Strengths
It is interesting to design an ansatz with favorable computational complexity.

### Weaknesses
1. To the reviewer’s best knowledge, the sorting algorithm in 3-dimensional space (more concretely, any spaces where the dimension is larger than one) is discontinuous. Thus, the proposed ansatz is discontinuous. When calculating the kinetic energy term, it is hard for the mcmc walkers to handle the energy near the discontinuous surface. As a result, the conventional energy calculation method in NN-VMC will lead to a non-variational energy result, which means the energy of the proposed method cannot directly compare with the other NN-VMC methods. 
 In section 1.2, the authors claim that some previous works ‘allude’ to a non-smooth ansatz. However, the corresponding ansatzes are smooth. The discontinuous property is just an assumption of the theoretical analysis. Therefore, those previous works do not suggest using a discontinuous ansatz. The authors must discuss more about the influence of the discontinuous property in the paper.

2. The computational cost of determinants is very small for the systems within 10 electrons. Thus, the acceleration achieved through the proposed ansatz is relatively small in those systems. To demonstrate the effectiveness of the proposed ansatz, the authors should study larger systems.

### Questions
The questions are listed in the weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers an important challenge in Quantum Chemistry, namely calculating the ground-state energy and its corresponding eigenfunction for gas-phase molecule. Recently, it was introduced to use neural networks as wavefunction parametrization in combination with Quantum Monte Carlo to solve this problem. A common issue is the scaling of the so-called Slater determinant to account for the anti-symmetry of the wavefunction. Evaluation of the Slater determinant scales cubically with the number of particles and therefore accounts for a significant part of the computational cost. The following paper proposes a new technique for anti-symmetrization (removing the necessity of evaluating the Slater determinant) with an improved scaling of O(N log N) with N being the number of particles. They show experimentally that for systems up to Bohr that they can reproduce state-of-the-art results and give a proof for weak universality of their ansatz.

### Strengths
The following paper considers a challenging topic of removing the dependency on the Slater determinant and by that trying to improve the scaling of recently proposed deep-learning-based wavefunction ansätze. Beside the anti-symmetry constrain of the wavefunction another complexity of the problem at hand is the need for highly accurate solutions. Normally, DL-VMC tries to recover the last 1-2mHa of the total energy. 

Therefore, the following paper has in my opinion three key strength:

-	Novelty: The paper introduces to the best of my knowledge a novel idea to reduce the scaling of the anti-symmetrization process. The idea looks promising, and it is able to recover state-of-the-art results, although only for small systems. 
-	The paper motivates the underlying problem and therefore introduces the topic to a broader community. (At certain parts I would have preferred a more detailed motivation, see weaknesses)
-	The proposed approach is underlined with a theoretical finding of the potential universality. Additionally, the paper discusses (in detail) their approach in comparison to other methods with similar scaling and motivates its potential strength.

### Weaknesses
One concern I have is regarding the claimed scaling of O(N log N) in the abstract. As stated in Sec. 3.1. it is more in the realm of O(N^2 log N) if not worse (see Fig. 3a).
A more detailed discussion about the need of expansions (K) would help improve the paper. With the current results it is difficult for me to assess if the scaling is actually as proposed.  

Although the paper motivates the problem and I am fine with the general structure of the paper, I have problems with the notation and explanation of certain concepts:

**Section 1.3. “Where did the determinants come from anyway?”**

Anti-symmetry is introduced in eq. (AS) but it is quite difficult to understand the eq. because:

- I couldn't find a definition of M.
- What does the up and down arrow represent?
- The positions of the electrons r are not introduced the first time they are used. 
- The anti-sym. (at least in the eq.) is only defined for spin-down electrons (or am I missing something?). 

**Section 3.1 “The Sortlet ansatz”**

The author might consider explaining their idea in more detail:

- In case of K>1 you are mapping the $\alpha$ functions to $\mathbb{R}^{N \times K}$, is this correct? 
- Eq. 7 you sum over K with $\alpha_i$, I am assuming the index i is not the same as in the introduction of the ansatz (eq. 6 and following bullet points)? 
- The exponential with factor $\gamma$ is to the best of my knowledge also new compared to prev. introduced wavefunction ansätze, where you would have an exponential envelope over the electron-nuclei distances. Could the author explain their design choices in more detail?
- In the complexity paragraph, they state $\alpha$ can be evaluated in $O(N^2)$. A short sentence that this is related to the computation of electron-electron interactions would give at least an intuition why this might be true. In my opinion this is especially difficult to understand for a reader who doesn’t know the PauliNet, FermiNet & PsiFormer papers in detail. 

I have additional (minor) comments regarding the notation (see “additional comments”). 
I want to stress I don’t think the paper needs to describe the whole field of DL-VMC but maybe the authors want to revise certain parts for better readability to reach a broader community. 

With the current weaknesses I am hesitant to recommend the paper to be accepted at ICLR. My decision is connected to the questions (see “Questions”) below because I am not convinced regarding the scaling, or in other words the number of expansions (K) needed for accurate results and it is difficult to assess with the given result section. 

**Minor additional comments:**

- The paragraph regarding the discussion of the different neural network architectures in Sec. 1.3. (around “…which is allowed non-symmetric…”) might be difficult to understand for a reader not familiar in detail with the work of FermiNet & PauliNet. 
The authors might consider adding additional details to better explain their argumentation (maybe in the SI). This is just a recommendation. I understand that it is not the task of the authors to explain the whole field of DL-VMC, but since the proposed ansatz requires quite a deep understanding of the topic it might be beneficial to add additional context. 
- Sec. 2.4 “Remark: Isn’t that estimate biased”: The authors write “the covariance between the two expectation in (4) via (23)”, do the author maybe mean (22) via (4) and not (23) ((4) and (23) seems to me to be the same equation)?
- In the proof of Prop. 4. We have n and N, I assume it should be both N?
- In the Hamiltonian you write $R_I$ but in the notation block $R_i$.

### Questions
- Can the author elaborate more on the scaling of their method? 
  - How large do you expect K to be? In Fig. 3a. it seems to be way more than linear. But since it is only one experiment it is difficult to assess.
- Do you have an intuition why your results are 0.5 Ha away from the FermiNet results for only a slightly larger system (compared to Bohr) for Nitrogen? You mentioned engineering problems, but this is difficult to assess without having a chance to look at the code (hopefully I didn’t miss a reference to the code).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In "Sorting Out Quantum Monte Carlo", the authors propose an antisymmetrizer for neural wavefunction ansätze in quantum Monte Carlo methods based on sorting. Compared to the typical antisymmetrization scheme based on determinants, which scales $O(N^3)$ with the number of electrons $N$, the proposed "sortlet" antisymmetrization has $O(N\log N)$ complexity. The overall complexity of evaluating a sortlet wavefunction is given as $O(N^2\log N)$ due to the $O(N^2)$ complexity of evaluating the $N$ terms $\alpha_i(r)$ used in the construction of a sortlet (Eq. 6). The proposed method is applied to variational quantum Monte Carlo calculations of atoms and small molecules with at most ten electrons and compared to an $O(N^2)$-scaling ansatz based on the Vandermonde determinant and the standard $O(N^3)$ antisymmetrization based on determinants. While the sortlet ansatz is superior to the Vandermonde ansatz in all cases and reaches chemical accuracy for some of the smallest systems, its performance for more complicated systems such as the methane molecule is significantly below the standard determinant-based ansatz.

### Strengths
The paper is well written and the proposed method clearly described. The section on variational quantum Monte Carlo is an excellent introduction for readers without a quantum chemistry education and makes the topic very approachable.

### Weaknesses
The proposed sortlet ansatz is only tested on very small systems. It performs significantly worse compared to the standard determinant-based ansatz for systems as small as the nitrogen atom (7 electrons). While the authors admit that this is the case ("our results are far from competitive with those of neural network ansatz with full determinant"), I do not agree with their statement that the proof-of-concept described in this paper is sufficient evidence that the sortlet ansatz is a promising direction and that their method could become competitive simply by means of additional investments in software engineering. The main problem I see is that the sortlet ansatz, which requires discontinuous $\alpha$ to be universal, is inherently at odds with using a neural network-based wavefunction, since neural networks are typically quite bad at representing discontinuities. From the results presented in the paper, it is unclear how the sortlet ansatz could be improved in the future to reach competitive results. I think the paper would benefit from additional experiments on larger systems (to assess whether the sortlet ansatz systematically becomes worse with increasing system size) and a detailed analysis *why* the ansatz fails (e.g. for nitrogen). The authors also do not provide sufficient evidence that the $O(N \log N)$ scaling of the sortlet antisymmetrization offers a practical advantage over the $O(N^3)$ scaling of determinant-based methods for the system sizes studied. It is not clear that the determinant calculation is the computational bottleneck for these small systems, and the authors should provide timing comparisons to support their claim that the sortlet approach is computationally advantageous. Furthermore, the performance of the sortlet method appears to degrade rapidly as the number of unpaired electrons increases, as seen in the atomic results. The authors should investigate this trend and provide a detailed analysis of why the method struggles in these cases. This analysis is crucial for determining whether further development of the sortlet ansatz is a worthwhile endeavor.

### Questions
1. The authors show that increasing the number of sortlets reduces the error w.r.t. the ground state for boron (Fig. 3a). How do similar curves look for the "failure cases" (e.g. nitrogen)? Is it possible to improve the results by simply adding more sortlets? If not, can the authors identify reasons *why* this is not possible?

2. The $O(N\log N)$ scaling of sorting versus the $O(N^3)$ complexity of computing a determinant is presented as one of the main motivations of the work. Given that the sortlet ansatz currently only works well for small systems, I wonder how large the computational advantage is in practice. I assume that for methods like FermiNet/PsiFormer, the calculation of the determinant is not actually the bottleneck (for small systems). I therefore suggest the authors show timing comparisons for training until chemical accuracy for the different methods (sortlet/Vandermonde/determinant).

3. When looking at the results presented in Fig. 2, in particular the results for the isolated atoms, it seems that the sortlet method starts to fail as soon as there is more than one unpaired electron in a given subshell. I suggest that the authors try to determine why this is the case. An analysis of the reasons why the sortlet ansatz fails would allow to judge whether it is reasonable to expect improvements with additional engineering effort in the future, or whether such an effort is futile. It might also allow insights into how alternative sub-cubic antisymmetrization methods could (or couldn't) be designed.

4. A very minor point about the use of "ansatz": There are several occurences of the word "ansatz" where the plural form "ansätze" would be the gramatically correct form (e.g. "when designing ansatz" should be "when designing ansätze" or "when designing an ansatz"). I suggest to change "ansatz" to the gramatically correct form "ansätze" where appropriate.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces an interesting neural-network architecture that is antisymmetric, for continuous input variables and potentially usable as an alternative to determinants in neural wave functions applications.

### Strengths
The paper is well written and describes the idea in good detail. It is also the first reported application of a sort-based idea that achieves chemical accuracy, at least on small systems.

### Weaknesses
The ansatz presented is still applied to relatively small systems. Also, I am fundamentally worried that given the discontinuity, the kinetic energy is not well defined (see questions). As a minor point, the discussion could be slightly improved, mentioning for example that second-quantized approaches are also determinant-free and based on sorting fermions (e.g. https://www.nature.com/articles/s41467-020-15724-9 ).

### Questions
Besides the small (minor) comment on the presentation/connection to determinant-free second-quantized approaches (see above), I mainly have two more in-depth questions : 

1. My understanding of this and related approaches is that the resulting wave function is not continuous in space. How does this affect the evaluation of the kinetic contribution to the local energy and how can the authors be sure that the resulting discontinuity does not affect the boundary conditions of the problem? It is indeed well known that if one has a singularity in the laplacian of the wave function, the energy can even violate the variational bound and be lower than the exact one. 

2. One appealing reason why Slater Determinants are used is because the non-interacting (or, better, mean-field) limit is exactly recovered by the Determinant form. Can the authors prove that a sortlet can efficiently recover (maybe even in a supervised way, if an analytical proof is not possible) the Hartree Fock limit?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
