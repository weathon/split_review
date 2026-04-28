# The Geometry of Phase Transitions in Diffusion Models: Tubular Neighbourhoods and Singularities

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 3, 8

## Abstract
Diffusion models undergo phase transitions during the generative process where data features suddenly emerge in the final stages. The current study aims to elucidate this critical phenomenon from the geometrical perspective. We employ the concept of ``injectivity radius'', a quantity that characterises the structure of the data manifold. Through theoretical and empirical evidence, we demonstrate that phase transitions in the generative process of diffusion models are closely related to the injectivity radius. Our findings offer a novel perspective on phase transitions in diffusion models, with potential implications for improving performance and sampling efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Under the data manifold hypothesis paper puts forward a geometrical perspective on diffusion models based on the concept of (maximal) tubular neighborhoods and manifold curvature. They derive a condition characterizing
the maximal radius (or more precisely the first injectivity radius) of the tubular neighborhood which is then exploited in an algorithm that allows its estimation.
They then provide some characterization of the direction of the score function on the boundary of a manifold neighborhood in the case of p_0(x) uniform on the manifold.
They then embark on a set of experiments on diffusion models, first with very simple synthetic datasets with simple geometries and then on some real datasets, 
claiming a connection between the injectivity radius and the dynamical phase transition (sudden changes of behavior) of the diffusion process (either reverse or forward).

### Strengths
The paper in principles would provide an interesting perspective on the temporal dynamics of the generative diffusion model based on the geometry of the data manifold and the concept of tubular neighborhood. They provide analytical and algorithmics tools to characterize the neighborhood. They perform experiments on good variety of synthetic datasets and investigate real dataset as well.

### Weaknesses
It is hard to understand the claims, due to vague or missing explanations, misleading captions and so on.

1. The main set of experiments relies on performing late initialization, which means if I understand correctly, 
run the reverse diffusion dynamics  starting from a time T which is generic and not large as usual, while the configuration
is still Gaussian generated. So the configuration at time T could be higly unlikely according to forward process.
Then they claim the a transition happens in T in some Wasserstein distance which they do not define, 
and this dependes on the radius of the tubular neightborhood and the fact that the particle enter the neighborhood.
This connection is not elucidated: what is the link between the radius and T? What does it mean to enter the neighborhood
and how it is related to the late initialization? The Wasserstein distance is among which distributions?
I must say that reading the manuscript without this very fundamental explanations has been a frustrating experience.

2. In this paper, the estimation of R2(M) is performed by def-
inition. -> "following the definition" or similar

3. prop. 3.4 names tubular neighborhood before defining it. Move definition c.10 to main?

4. In section 3 the algorithm exploiting Theorem 3.7 to estimate R1 is not clearly stated.

5. In eq. 9, s is supposed to be t instead?

6. Section 4 should convey more intuition on what the propositions imply.

7. Table 1. Honestly based on the caption "Wasserstein distances W for different late initialisation times. ρproportion represents the proportion of particles outside the tubular neighbourhood." I cannot understand 
the content of the table. It doesn't seem consistent. The column names are supposed to be proportions (maybe in percentage?) or initalization times? 

8. Section 5: "In this section, we empirically demonstrate the presence of phase transitions at the boundary of the
tubular neighbourhood during the generative process of diffusion models. In particular, we analyse
the proportion of particles outside the tubular neighbourhood at each time step and examine the
corresponding changes in the Wasserstein distance."" -> Wasserstein distance among which distributions?

9. proposition 4.2: f(t,x) -> f_t(x) for consistency with Eq. 3. Same for g
10. Authors start talking about phase transitions at the beginning of Section 5, but at these point things are not clear. Which kind of phase transitions? What is changing? Which is the order parameter?
11. What is the vertical line in Fig. 4. It is not explained in the caption...
12. Captions for Fig. 4 and similar, should explaing that the x axis referes to the the "late initialization" time of the reverse process, with T=1000 corresponding to the usual initialization time.

### Questions
1. The main set of experiments relies on performing late initialization, which means if I understand correctly, 
run the reverse diffusion dynamics  starting from a time T which is generic and not large as usual, while the configuration
is still Gaussian generated. So the configuration at time T could be higly unlikely according to forward process.
Then they claim the a transition happens in T in some Wasserstein distance which they do not define, 
and this dependes on the radius of the tubular neightborhood and the fact that the particle enter the neighborhood.
This connection is not elucidated: what is the link between the radius and T? What does it mean to enter the neighborhood
and how it is related to the late initialization? The Wasserstein distance is among which distributions?
I must say that reading the manuscript without this very fundamental explanations has been a frustrating experience.

1. In this paper, the estimation of R2(M) is performed by def-
inition. -> "following the definition" or similar

1. prop. 3.4 names tubular neighborhood before defining it. Move definition c.10 to main?

1. In section 3 the algorithm exploiting Theorem 3.7 to estimate R1 is not clearly stated.

1. In eq. 9, s is supposed to be t instead?

1. Section 4 should convey more intuition on what the propositions imply.

1. Table 1. Honestly based on the caption "Wasserstein distances W for different late initialisation times. ρproportion represents the proportion of particles outside the tubular neighbourhood." I cannot understand 
the content of the table. It doesn't seem consistent. The column names are supposed to be proportions (maybe in percentage?) or initalization times? 

1. Section 5: "In this section, we empirically demonstrate the presence of phase transitions at the boundary of the
tubular neighbourhood during the generative process of diffusion models. In particular, we analyse
the proportion of particles outside the tubular neighbourhood at each time step and examine the
corresponding changes in the Wasserstein distance."" -> Wasserstein distance among which distributions?

1. proposition 4.2: f(t,x) -> f_t(x) for consistency with Eq. 3. Same for g
1. Authors start talking about phase transitions at the beginning of Section 5, but at these point things are not clear. Which kind of phase transitions? What is changing? Which is the order parameter?
1. What is the vertical line in Fig. 4. It is not explained in the caption...
1. Captions for Fig. 4 and similar, should explaing that the x axis referes to the the "late initialization" time of the reverse process, with T=1000 corresponding to the usual initialization time.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new viewpoint that the boundary of the tubular neighborhood of the underlying data manifold. This is an intuitively justifiable claim worth pursuing. However the arguments in the paper are not sufficiently solid.

### Strengths
The authors defined tubular neighborhoods and their injective radius, and proposed formulas (Theorem 3.7) to compute these radii. They also proves that the score vector fields at the boundary always point towards the interior of the neighborhood, i.e. diffusion trajectories tend to be attracted into the neighborhood.

### Weaknesses
There are a few of flaws in the paper's reasoning in my opinion.
1. The paper doesn't define what a phase transition actually means or propose hypothesis on mechanism behind it. In particular, what makes the tubular neighborhood special among all neighborhoods? The message delivered by what is currently written is rather "trajectories will eventually enter the tubular neighborhood" and "some kind of phase transition occurs when trajectories get closer to the data manifold". However the same can also be said about neighborhoods of different radii. It would be helpful if there could be an argument supporting that transition starts once points enter the tubular neighborhood, or once they are sufficiently close by another unknown standard. For example, in Figure 5, it is not obvious whether the transition points match between the red and blue curves. 
2. The paper uses an oversimplified setting of a single injective radius for all points in the manifold. However, because: (i) the validity of manifold hypothesis in full generality is questionable see e.g. "Verifying the union of manifolds hypothesis for image data" (Brown et. al ICLR 2023) and intrinsic dimensions may vary among data points, (2) even assuming the manifold hypothesis, in practice the manifold is usually very wiggly, resulting in high variance in both R_1(M) and R_2(M). What "entering the tubular neighborhood" means might become ambiguous in such a setting. 
3. The experiments uses a simple setting of unit spheres with an intrinsic radius of 1. This setting is not very helpful because the intrinsic radius is critically determined at the origin, while in the actual diffusion model experiment, the majority (or at least a large percentage) of points approach the sphere from the outside, they don't really "see" the injective radius in the whole process. The emphasis on the injective radius in this case merits more explanation. Similar problem exists in the experiments on ellipses or tori. For instance, for ellipses, the injective radius is determined by the length of the short axis and the principal curvature at the end of long axis, and again the majority of trajectories will approach the manifold without out seeing these factors at all. For the experiments with MNIST and FMNIST, I think the method of embedding them into S^d  ignores their own intrinsic geometries and is inadequate, precisely by the authors's own analysis at the beginning of Section 5.4. Namely the datasets's intrinsic geometry is what matters here, a spherical embedding doesn't change the property that the intrinsic radius is small (and varying drastically among data points). Embedding it into S^d and pretending to have a fake injective radius of 1 completely disconnects the analysis from the reality for actual diffusion processes near the data distribution.

### Questions
1. The experiment results record "Wasserstein distances W for different late initialisation times". You should tell the reader this is the Wasserstein distance between which two distributions. Why is it increasing when t->0? (When assessing diffusion models, one often look at Wasserstein distance between the generated distrbution and the ground truth one, which is suppose to decrease as t->0.)
2. R_1(M) should be closely related to the reciprocal of the largest principal curvature at each point. Reference: Section 4 from "Reconstruction and interpolation of manifolds I: The geometric Whitney problem", Fefferman et al. 2021 .

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the phase transition phenomena in the generative process of diffusion models from a geometric perspective. The authors first define the injectivity radius, characterize it as the minimum of the first and second injectivity radii, and propose a practical algorithm for estimating the first injectivity radius. Subsequently, the paper computes the proportion of probability mass within the tubular neighborhood and the Wasserstein distance using the late initialization scheme. Through various experiments involving toy models and the MNIST dataset, the paper concludes that the phase transition corresponds to a rapid decrease in the proportion of particles outside the tubular neighborhood and a sharp increase in the Wasserstein distance. This study illuminates how geometrical structure interacts with the training and inference process of diffusion models, paving the way for further research to develop specific algorithms accordingly.

### Strengths
- The paper presents a novel perspective that establishes a connection between the geometric characteristics of the data distribution and the phase transition phenomena observed in the Wasserstein distance during the generative process of diffusion models.
- The paper presents rigorous mathematical arguments and definitions for all concepts introduced in this context, including the injectivity radius and tubular neighborhood. These arguments provide a solid foundation for the experimental reasoning presented in the paper.
- The paper presents compelling experimental evidence that demonstrates the correlation between the increase in the Wasserstein distance and the proportion of particles within the tubular neighborhood.

### Weaknesses
 - The paper’s scope remains confined to toy models, and there are several instances where the experimental outcomes deviate from the conjectured behavior.
- The algorithm for computing the injectivity radius and the proportion of particles within the tubular neighborhood lacks a clear and comprehensive description. Algorithm 1 requires revision.
- The Wasserstein distance is not explicitly defined between which two probability distributions it is measured.

### Questions
Despite the promising experimental results, I remain uncertain about the direct relationship between the increase in the Wasserstein distance and the proportion of particles within the tubular neighborhood. My primary concern is that:
- The injectivity radius appears to be fixed for a specific data distribution. Consequently, for any chosen radius (which may or may not be the injectivity radius), a corresponding tubular neighborhood can be defined. Furthermore, based on my understanding, the red curves in all the figures exhibit a similar trend, given the characteristics of the forward process. So it is unclear if the injectivity radius defined in the paper is a pivotal factor for this phenomenon to appear.
- In several experiments, the timing of the increase in the Wasserstein distance does not precisely align with the 0.99 threshold. This suggests that the conjecture may be attributed to a coincidental association with the exponential diffusion of singularities in the OU process.

To strengthen the conjecture, additional experiments are necessary to provide corroborating evidence. These experiments could include:
- Statistical and quantitative evaluation of the correlation between the Wasserstein distance and the proportion within the tubular neighborhood.
- Experiments conducted on a family of datasets with varying injectivity radii, where the corresponding curves are observed and their relationships with the injectivity radii are assessed.
- Reparameterization of the inference process to extend the final portion, enabling a more precise observation of the phase transition.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a detailed geometric analysis of spontaneous symmetry breaking phenomena in generative diffusion models under the manifold hypothesis. To go beyond the very symmetric cases discussed in (Raya, 2023), the authors study the injectivity radius of the manifold, which is the supremum of possible radii of tubular neighborhoods of the manifold. The main idea is that, if at time t the probability mass of the forward kernel is mostly inside the maximal tubular neighborhood, then  all 'generative decisions' are already been made and the particles are projected by the score with high probability on a single well-defined target point. 
Therefore, at least locally, there will be a finite value of t at which the symmetries of the generative process break spontaneously, meaning that, around a given point of the manifold, the distributions of the generative paths collapse on deterministic targets. 
The authors show that these local phase transitions depend on the curvature of the manifold, with higher curvature leading to later critical collapse times. This time corresponds to the disappearance of singularities (i.e. points of non-smoothness) on the epsilon-neighborhood of the manifold.

The paper contains both theoretical results and experimental analyses on real datasets. The main result of the theoretical analysis is the characterization of the critical times based on the local curvature. The experiments show the results of late initialization as a way of detecting the first symmetry breaking event as introduced in (Raya, 2023). The authors carefully control the geometry of the target data and the deviation of the distributions in order to control the phenomenon of mean and covariance shift prior to the symmetry breaking event.

### Strengths
The paper successfully addresses the main limitation of the theoretical approach used in (Raya, 2023), namely that the analysis of the fixed points is only practical in highly idealized models.
The analysis of the injective radius of the tubular neighborhood offers a very precise and powerful tool to characterize more complex symmetry breaking phenomena that can better capture the richness of real data. These new tools offer an important stepping stone in our theoretical understanding of generative diffusion and its relations with fundamental concepts in statistical mechanics and differential geometry.

The theoretical analysis has the rare property of being both rather rigorous and beautifully intuitive. The figures work extremely well in explaining the main ideas from a visual geometric perspective. On the other hand, the mathematical structure allows for precise calculations to match these intuitions. 

The experimental results are not spectacular but they offer a solid validation of the main ideas. I appreciated the breath of the geometric configurations that have been studied and the effort to rigorously control potential confounds.

### Weaknesses
I think that the main missing link in the paper is a direct connection with the fixed-point method used in (Raya, 2023). In geometric settings, if the data distribution is uniform when restricted to the manifold, it is possible to define the latent manifold at time t as the set of stable fixed points of the vector field, i.e. the minima of the potential energy function. 
Intuitively, the appearance of a singularity in your framework should correspond to the 'collapse' of a portion of the data manifold into a single point in the latent manifold at time t, this is equivalent to the bifurcation of isolated fixed-points corresponding to Curie-Weiss type transitions. For example, it is easy to see that a hyper-sphere collapses into a single latent point when the injective radius is exceeded. 
In the general case of unequal curvature, I would surmise that this phenomenon happens locally. 
It would therefore be very insightful to study how these geometric singularities correspond to the geometry of the potential energy function, which will connect the theory more directly with the theory of critical phase transitions in physics.


I see two further weak points in the analysis, which however could be addressed in future work.

1) While it is interesting to study the first symmetry breaking event as the main phase transitions, it would be insightful to provide a more detailed analysis on the multiple critical times that arise in manifolds with non constant curvature. Under your model, the first critical time corresponds to the disappearance of the singularities around the points with the highest curvature. This is the first visible symmetry breaking event and it therefore demarcates the first main deviation from approximate Gaussianity in the marginal distribution, as visible from the late initialization curves.
While this effect is very visible and very important in the generative process, it is not necessarily more conceptually important than the further critical times corresponding to regions with lower curvature. In fact, at least locally, these correspond to other genuine critical transitions where important 'generative decisions' are made to spontaneous symmetry breaking events.

While the theory can be easily applied to the analysis of these subsequent transitions, I would have appreciated direct experimental verification of these events under controlled conditions. Note that this would required a different approach than that used in the late initialization experiments. 

2) It would have been very nice to have a characterization of the phase transitions in this geometric setting in the language of statistical physics, since the connection with (Raya, 2023) suggests a deep link. However, I assume that the lack of details on the physics side comes from the background of the authors and it can be remedied by future work on the subject.

### Questions
1) Could you provide a theoretical connection between your geometric method and the fixed-point analysis presented in (Raya, 2023)?

2) Could you expand your experiments to provide evidence of separate transition times in manifolds with defferent local curvatures?

### Soundness
4

### Presentation
3

### Contribution
3
