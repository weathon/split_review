# Enforcing Latent Euclidean Geometry in VAEs for Statistical Manifold Interpolation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Latent linear interpolations are a powerful tool for navigating the representation space of deep generative models. This aspect is particularly relevant in applied settings, where meaningful latent traversals can be learnt to represent the evolution of a system's trajectory and mapped back to the often complex and high-dimensional data space. However, when data lies on a manifold with complex geometry, linear interpolations of the representation space do not directly correspond to geodesic paths along the manifold unless enforced. An example of such a setting is scRNA-seq, where high-dimensional and discrete cellular data is assumed to lie on a negative binomial statistical manifold modelled by the decoder of a variational autoencoder. We introduce FlatVI, a novel training framework enforcing Euclidean geometry in the latent space of discrete-likelihood variational autoencoders modelling count data. In our regularisation setting, straight lines in the latent domain correspond to geodesic interpolations in the decoded space, improving the combination of our model with methods assuming Euclidean latent geometry. Results on simulated data empirically support our claims, while experiments on temporally resolved biological datasets show improvements in the reconstruction of cellular trajectories and the learning of biologically meaningful velocity fields.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript is on learning a specific representation tailored to learn dynamics, specifically arising from scRNA-seq. The authors regularize the latent space of a VAE, by the geodesic of a statistical manifold. This way, straight lines in the latent space correspond to geodesics on the statistical manifold. The authors showcase the advantages of the method on toy datasets with known geodesics and scRNA-seq datasets.

### Strengths
The presentation of the paper is easy to follow and the method is clearly explained. I like that the authors test their methods on simulated data and real word data. The method is founded on a strong theoretical background.

### Weaknesses
In table 1, it is hard to understand the scale of the MSE (Geo-Euc). We understand that $\lambda = 7$ is better than $\lambda=0$, but maybe $8.02$ is still bad. It could be interesting to look at global and local properties that are preserved with the distance matrix. For example, include additional analyses such as Spearman correlation between the ground truth distance matrix and the one from predicted geodesics, or the overlap between k-nearest neighbors of the two distance matrices. This will give a more comprehensive view of how well the geodesic distances are preserved.

In Figure 2, it is hard to interpret, especially the columns a) and b). What should we expect for a Euclidean space? If I understand correctly, both VoR and CN should be uniform on the latent space. It may be beneficial to add these features on a Euclidean space, so that the reader can visually compare the different representations. 

In Figure 2, some points in the FlatVI model still show large VoR and CN values. Could you provide an explanation for why these points persist despite the flattening regularization? Additionally, it would be informative to show examples of geodesics between points from high VoR regions in the FlatVI latent space to demonstrate whether they are indeed straight lines as expected. Consider including a brief discussion of potential reasons for these high VoR and CN points in the FlatVI model.

### Questions
Minor comments and questions;

- In Table 1, consider renaming the 'Model' column to 'Lambda' to more accurately reflect the variable being compared across rows.
- I find Figure 2 a bit hard to interpret, especially the columns a) and b). What should we expect for a Euclidean space? If I understand correctly, both VoR and CN should be uniform on the latent space. It may be beneficial to add these features on a Euclidean space, so that the reader can visually compare the different representations. 

- In Figure 2, some points in the FlatVI model still show large VoR and CN values. Could you provide an explanation for why these points persist despite the flattening regularization? Additionally, it would be informative to show examples of geodesics between points from high VoR regions in the FlatVI latent space to demonstrate whether they are indeed straight lines as expected. Consider including a brief discussion of potential reasons for these high VoR and CN points in the FlatVI model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper generalizes the Riemannian structure for the statistical manifold with Fisher Information Metric (FIM) to a flattened version and solves OT-CFM problem. More specifically, it proposes a regularizer $\mathcal{L}_{flat}$ which penalizes the curvature from $M$.

### Strengths
The paper shows improvement in many applications, including simulated data and real biological problems. Good performance is shown.

### Weaknesses
My current understanding is: the main contribution is only adding a regularizer $||M-I||$. I would think it is an incremental contribution, since the definition of ELBO and $M(z)$ are both known. I understand this forces the ELBO loss to become Euclidean loss, but I need some help understanding the main contribution better.

Could you also elaborate on the novelty and significance of applying this technique specifically to statistical manifolds and single-cell RNA sequencing data, please?

Could you please explicitly state which parts of Sections 3 and 4 are novel contributions versus background or existing work? I am not an expert but it seems to me that all the contents in Sec 3 and 4 are existing results except Eq. 11 and 12. It would be helpful if you could highlight the key innovations other than the regularization term.

Tiny typo: there is an extra comma in line 259

### Questions
Could you please explicitly state which parts of Sections 3 and 4 are novel contributions versus background or existing work? I am not an expert but it seems to me that all the contents in Sec 3 and 4 are existing results except Eq. 11 and 12. It would be helpful if you could highlight the key innovations other than the regularization term.

Tiny typo: there is an extra comma in line 259

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a regularization of variational autoencoders (VAEs) such that the natural representation geometry is flattened. This makes shortest paths (geodesics) near-linear, such that optimal transport dynamics are more readily applicable (OT dynamics often rely on straight-line interpolants). The work is demonstrated in the single-cell regime and results are promising.

### Strengths
* The paper provides a sound and sensible combination of techniques from VAEs, differential geometry, and optimal transport.
* The proposed model allows for more reliable data interpretations, which is important e.g. in the studied life science domains (but also in other domains).
* The paper is easy to follow and generally well-written.

### Weaknesses
## Communication
* It is not always entirely clear what the actual contribution of the paper is and what was previously known. For example, the introduction states that "In particular, no prior work has extended existing frameworks for learning latent geodesic trajectories to statistical manifolds of
discrete probability distributions", but this is exactly what the "Pulling back Information geometry" paper did. The present paper has significant novelty over the "Pulling back information geometry" paper, but the communication becomes unclear in terms of what constitutes the contribution.
* The paper is often phrased to indicate that the fitted model will have an Euclidean latent geometry. This is obviously incorrect. What the paper actually does is regularize towards Euclidean geometry. This is merely a matter of phrasing things differently, but I would appreciate more clarity here.

## Computations
* As far as I can tell, differentiating through the regularizer (Eq. 11) will be a bit expensive as it requires higher-order derivatives of the decoder.

### Questions
* The "Pulling back Information Geometry" was able to avoid differentiating through the metric by instead approximating it locally with the KL. Is something similar feasible to make optimizing Eq 11 cheaper?
* Will code be made available?
* A big part of prior work on latent representation geometries focuses on how model uncertainty seems to reflect the topology of the data manifold. As far as I can tell, the presented approach is not influenced by model uncertainty. Is this correctly understood? If so, would it be difficult to incorporate uncertainty?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors consider the approximation of a manifold by a VAE. Here, they introduce a new regulariser for the training loss which enforces that geodesics on the learned manifold correspond to straight lines in the latent space. They pay particular attention to an application with cellular data from computational biology.

### Strengths
The regulariser of the loss function is well-motivated by the pull-back of the Fisher-Information-Geometry. At the same time it is simple to implement and seems to be effective. Also the application looks sensible, but I have to admit that it is a bit out of my own expertise (therefore the low confidence of the review).

### Weaknesses
During reading the paper I came across a couple of confusions and comments, which I list below. Summarising, I think that this paper needs some improvements about its assumptions and the clarity of writing. In the case that the authors improve the paper during the rebuttal, I am willing to reconsider my evaluation.

## Confusion about the kind of manifolds which is considered

The authors mention at several points of the paper that they consider manifolds "with complex geometry". The authors should specify what is meant by this term. For instance, there is no chance to approximate a manifold with holes (like in Fig 1) with a single latent space, since there exists no homeomorphism between two spaces of different topology. 

As a simple example in intuitive language: when we can consider the $\mathbb{S}^1$ embedded in the $\mathbb{R}^2$ and approximate it by a VAE with one-dimensional latent space, we have to "wrap the line around the circle". This leads to a point, where "the two ends of the line meet". In particular, there exist points which are very close in the data space, but far away from each other in the latent space.

In particular, in the general case, geodesics might not exists or might not be unique. In both cases, the representation with a flat latent space is not possible. 

## Evaluation of the flattening loss

The authors should evaluate the proposed flatting loss in a lighter setting, where the results can easily be visualised. One suggestion for such an experiment could be the following:
Take a two dimensional exapmle manifold embedded in the $\mathbb{R}^3$ (e.g., the torus, sphere, swiss roll, etc.) and learn a VAE with different flattening loss regularisation strengths (and the Riemannian metric inherited from the space where the manifold is embedded in). Then, take some points on the manifold located opposite of each other, connect them by a straight line in the latent space and plot the resulting path on the manifold. If the flattening loss works properly, these lines should become more regular for stronger regularisation.

## Clarity of the model

The paper could benifit a lot from a complete and formal description of the model somewhere in the beginning, answering the following questions: What kind of data is given? From where to where maps the decoder (so what is the manifold and how does it relate to the data)? Where comes the time dynamics into play?

The description in Section 3.1 is insufficient. For example, I came across the following confusions:

- please define $\mathcal X$ and $\mathcal Z$.

- $\phi$ denotes at the same time a variable from the parameters space of $\mathbb{P}$ and the paramteres of the decoder. This is not a very good style. In particular, in (2) there appears the expression $p_\phi(x|h_\phi(z))$. Inserting the definition of $p_\phi$ from (1), this is equal to $\mathbb{P}(x|h_\phi(h_\phi(z)))$, which is most certainly not, what the authors meant.

Even though these errors are minor and most readers should be able to figure out what is meant, they make the paper really hard to read.


## Minor comments

- The notations from Sec 3.2 require that the decoder is a diffeomorphism between the latent space and its image. In this setting this corresponds to the property that $\mathbb{J}_h(z)$ is full-rank for all $z$ from the latent space. While I think that it is common to ignore this assumption for numerical computations, this should be mentioned.

- In Section 3.2: It is a bit odd to cite recent research papers for classical concepts for differential geometry. It would be better to refer to some general text book (like these research papers do).

- eqt (11): please specify the used norm.

- Fig 1: Why does the visualisation of the VAE interpolation map to a point outside the learned manifold?

- Probably evaluating the flattening loss is slower than the usual VAE loss since it requires differentiating twice insted of once through the decoder (once for computing the FIM and once for taking the gradient). Is that correct? If yes, this should be mentioned somewhere (even though I don't believe that this limitation is too important).

- line 323: Please specify the parameter space ($\theta,\mu>0$?)

### Questions
I state already plenty of questions in the weaknesses part. Additionally, I wondered how the approach scales with the dimension of the manifold, and in particular with the dimension of the space where it is embedded in. Is the approach feasible for high-dimensional manifolds? I guess that at some points the matrix-vector multiplication for the Gram matrices become expansive. Which dimension range is mainly targeted by the authors?

### Soundness
2

### Presentation
2

### Contribution
2
