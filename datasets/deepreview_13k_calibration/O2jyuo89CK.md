# Modelling complex vector drawings with stroke-clouds

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Vector drawings are innately interactive as they preserve creational cues. Despite
this desirable property they remain relatively under explored due to the difficulties
in modeling complex vector drawings. This is in part due to the primarily _sequential and auto-regressive nature_ of existing approaches failing to scale beyond simple
drawings. In this paper, we define generative models over _highly complex_ vector
drawings by first representing them as “stroke-clouds” – _sets_ of arbitrary cardinality comprised of semantically meaningful strokes. The dimensionality of the
strokes is a design choice that allows the model to adapt to a range of complexities.
We learn to encode these _set of strokes_ into compact latent codes by a probabilistic
reconstruction procedure backed by _De-Finetti’s Theorem of Exchangability_. The
parametric generative model is then defined over the latent vectors of the encoded
stroke-clouds. The resulting “Latent stroke-cloud generator (LSG)” thus captures
the distribution of complex vector drawings on an implicit _set space_. We demonstrate the efficacy of our model on complex drawings (a newly created Anime
line-art dataset) through a range
of generative tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper purports to present a method for generating _vector representation of complex sketches_.
The problem is important and has the following challenges:
1. most work on generative modeling focuses on images, so vector representation is underrepresented.
2. the number of _strokes_ within each sketch is variable.
3. autoregressive methods using a sequence representation fail to scale up.
4. the sequence representation is sensitive to the ordering of strokes.

---

The claimed contributions are:
1. proposing the first method for generating _highly complex drawings_.
2. using a _set representation_ instead of a sequence representation.

---

The paper:  
1. (MAJOR) argues that a set representation is is theoretically possible because  of  `De Finetti General Representation Theorem` which states that for an `exchangeable` set with a pdf for each of it's constituent sets (one realization of the permutation), there exists a pdf that describes all the permutations in the limit.
2. (MAJOR) presents a practical way to construct this permutation-invariant pdf, so that we can sample sketches from this distribution tractably.
3. (MINOR) presents a new dataset called `Anime-Vec10k` which which is significanlty more complex than existing datasets (notably QuickDraw!)

---

The method used to achieve the goal of  "generating _vector representation of complex sketches_" is roughly the following:
1. Consolidate image into sets of bezier-curves.
2. Use a Set-Encoder to encode the stroke-set to get a latent.
3. Use a VAE loss to regularize the space of latents.
4. Use an MLP based conditioning denoising network to get from (500/1000) _random_ strokes to the actual strokes.
5. The important point in point 4 is that **each stroke is considered iid**.

### Strengths
**The problem setting is valuable to the community.** 

---

While diffusion models have been providing very high quality generative models in the raster world, they have not made as much of a splash in the vector world. So I commend the authors for tackling this problem.

**Very good exposition.**

---

The paper is very easy to follow. While the abstract could possibly use some more technical details. Everything from the introduction on flows logically. The introduction is superb, even though it spends a bit more time describing why `creational` representations matter than I would have liked. The introduction still sets up the problem well - the problem with sequences (ordering and non-scalability of the autoregressive approach) and the problems with using a set approach (variable and unknown cardinality). The related work section is quite comprehensive to me. I would still like to suggest two references which might be interesting to the reader in the weaknesses section.

**The core idea is simple to implement**

---

The whole paper is based on simple building blocks, so any (re-)implementation should be easy.

### Weaknesses
While I like the paper, in its current form the paper has many weaknesses:

**(MAJOR): Sampling issues**:

---

The authors clearly point out that the number of strokes is an issue, but simply brush it away by saying we use 1000 strokes.
This is a glaring flaw. What if the sketch is simpler? What happens to the other strokes? Are they duplicated? 

The discussion in Appendix E is is simply not enough to provide a solution.

**(MAJOR): Matching issues/ iid assumption of strokes **:

---

Related to sampling is the issue of matching. In the diffusion model equation (3), you simply decompose the sketch into iid strokes. This is a **VERY** strong assumption. I do not see how during sampling, one cannot get a degenerate solution of just repetetively denoising into the same stroke. There is no question asked about how the iid sampling affects the proposed pipeline.

In the same way, how is the sequence $\mathbf{s}$ generated at training time? Do you let the randomness of the random strokes take care of matching the proper final stroke? Why is there no hungarian matching? Assuming normalized coordinates in $[-1, 1] \times [1, 1]$ , how does it make sense for the denoising network to take a random stroke at (-1, -1) and try to denoise it to (1,1), instead of just recognizing (with hungarian matching) or simple euclidean distance that it is much easier to denoise the stroke closer to the final location?

**(MAJOR):  Sequence representation/Sequence lengths**

---

It is not clear at a first glance (unless I am wrong) that the paper does the following:
1. Takes in a **variable** number of input strokes
2. Generates (denoises) a **fixed** (1000) number of output strokes.

The motivating factor of the paper, and the way the paper is currently written suggest that the model is capable of generating a variable number of strokes. It seems that is not possible

**(MAJOR) No quantitative results**

---

I said previously that the paper has missing citations. I will mention the actual links later but describe them here:

There has been recent work (<1.5years) in the autoregressive generation area. The work is based on how to make generation permutation invariant which is exactly the problem being tackled here. There are two papers in this area: [Paschalidou] and [Para]. [Paschalidou] use a learnable query vector that looks at the previously generated sequence and predicts the next one. [Para] uses a set encoder and a sequence decoder with mask tokens to perform controled generation.

The authors do not cite these papers. The authors have no baselines as they (rightfully) claim that previous work does not scale - but there [Paschalidou] has code available and it would be easily adaptable to their current training regime

[code](https://github.com/nv-tlabs/atiss)

All you have to do is make each token the sum of its control point embeddings! And then introduce some form of conditioning - either a single condition token or an encoder as done in [Para].

This should significantly strengthen the paper - we see exactly how slow and underwhelming the other methods are, how slow to sample, what the FID is, and qualitative results as well. I would really like to see those result

**(MINOR)  Few qualitative results**

---

While there are a decent number of qualitative results in the paper already - the dataset itslef is small - 10k samples. I would request the authors to **check for overfitting** by also visualziing the closest training set example to each generated sample - this could be in the rgb space as well as some perceptual space - look at the sketch retrieval literature or just VGG features.

Another thing that will help both analyze the dataset quality and the generation quality is to have a big 10x10 grid from both sets (trainig and generation) somehwere in the paper

**Missing citations**

The missing citations are 
1. @Inproceedings{Paschalidou2021NEURIPS,
  author = {Despoina Paschalidou and Amlan Kar and Maria Shugrina and Karsten Kreis and Andreas Geiger and Sanja Fidler},
  title = {ATISS: Autoregressive Transformers for Indoor Scene Synthesis},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year = {2021}
}
2. @inproceedings{10.1145/3588432.3591561,
author = {Para, Wamiq Reyaz and Guerrero, Paul and Mitra, Niloy and Wonka, Peter},
title = {COFS: COntrollable Furniture Layout Synthesis},
year = {2023},
series = {SIGGRAPH '23}
}


### Questions
I already asked most questions.

1. Figure 5: Why does the DDPM sampler seem to have more strokes than the DDIM sampler? or are the strokes just placed closer together in the DDIM sample?

2. Do you plan to release the dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method using Diffusion Models and  Set Transformer for generating sketchs of Anime girls in vector format.
The training data is obtained by transfering raster images into vector curves.
The generation module contain two parts, the Stroke cloud Representation Module (SRM) and the Latent Stroke cloud Generator (LSG). 
The LSG module is a diffusion model, which serves to sample latent codes. Each latent code corresponds to a sketch result. 
The SRM module contain two parts:
The first part is a Set Transformer, which serves as an encorder to encode training datas into latent codes.
The second part is a diffusion model, which serves as an decorder to generate sketch strokes conditioned on the latent code.

### Strengths
1. The idea of applying the Set Transformer to encode the stroke data is the most significant advantage of this paper. The nature of the Set Transformer theoretically guarantees permutation-invariant, so that all the strokes in one sketch can be encoded into a latent code to represent the sketch without worrying about the order of the strokes. This encoder also works even if the stroke number varies among the sketches in the dataset.

2. Also thanks to the Set Transformer, the decoder of the SRM module can sample arbitrary numbers of strokes to constitute a sketch.

3.  Although this paper focuses on the topic of sketch generation. I see the potential of this method to be applied to other artistic styles such as oil painting, just needs to change the stroke model and the dataset.

### Weaknesses
1. I think the main weakness of this paper is the poor visual quality, which is far from artistic application. And the stroke design of the Bezier curve is too simple.  Could the Bezier curve contain more parameters such as width and transparency? The limited complexity of the Bezier curves, specifically using only quadratic curves, restricts the expressiveness of the generated sketches. This is a significant limitation, as more complex curves with additional control points and parameters would allow for a richer variety of stroke shapes and styles, which is crucial for artistic applications. Furthermore, the lack of control over stroke width and transparency limits the ability to create depth and variation in the sketches, further contributing to the poor visual quality.

2. Lack of comparison. I do recognize that there may be no methods similar to your technique route. But you should compare with at least one method related to the topic of sketch generation, even though there may be raster-based such as GANs. The absence of a quantitative comparison with existing sketch generation methods, even raster-based approaches, makes it difficult to assess the relative performance and advantages of the proposed method. While the authors acknowledge the novelty of their approach, a comparison with at least one baseline method is necessary to provide context and demonstrate the effectiveness of their technique. This is especially important given the stated goal of artistic application, which requires a clear demonstration of superiority or at least comparability to existing methods.

3.  There seems to be a flaw in the experiment of section 4.4, figure 8. I can see the sketches corresponding to the interpolated results in Figure 8 (the middle ones) are obviously not in the correct domain. This may be because your interpolation function does not fit this distribution (and I didn't see your interpolation function), which leads to the interpolated latent codes are not on their true distribution（you can analogy the manifold of Swiss Roll). The interpolation results presented in Figure 8 raise concerns about the latent space representation. The fact that the interpolated sketches appear to be out of the correct domain suggests that the latent space may not be smooth or well-structured. This could be due to the interpolation method used, or it could indicate a more fundamental issue with the training process or the architecture of the model. Without a clear explanation of the interpolation function and a more thorough analysis of the latent space, it is difficult to determine the root cause of this problem.

### Questions
This question is just for discussion (doesn't affect my rating):
How do you critique the technique route that transfers raster images into vectors? Just as your method of establishing your dataset.
I mean, people can use raster image generation tools such as Stable Diffusion to generate a raster image, and then transfer it into SVG format (the recent work of VectorFusion follows this idea). Compared with this technique route, what's the advantage of your technique route? Or in other words, do you think directly generating vectors is more prospoective?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The idea is to model a vector drawing as a _set_ of strokes.
Drawings are created by a diffusion process to create a “stroke cloud”.
The strokes are represented in a low-dimensional latent space, making them conditionally independent.
The paper tackles an interesting problem in a novel and principled way.
It produces reasonable results.
It is of publishable quality.

### Strengths
Introduction:
Differentiates between vector and pixel representations, and claims the former is pressed (somehow)
on creativity while the latter is based on perception. These claims I have weak sympathy with, but
which I don’t fully agree with (surely people draw with lines/vector because that is how they perceive
the world). The are made without any citation into either the perceptual or artistic / art-history literature.
And they pervade the first part of the paper, making slightly uncomfortable reading for me - feeling that
the argument made may even mislead. I’d like to see it changed, but given my greater sympathy towards
the use of vectors over pixels, it’s not something I will insist upon other than “think again about the argument”.

Related Works:
The paper touches upon only a very small fraction of the available literature, and fails to cite any paper prior to 2015 - even though there is a large body of work (see the non-photorealistic rendering literature).
More on this later.

Method
The method is to represent a drawing with a set of strokes, the exact number does not matter.
I very much like the fact the authors acknowledge strokes are not independent, but use 
De-Finetti’s Theorem of Exchangeability - which I am not familiar with (so thanks for the introduction)
so that they are conditionally independent.

I am less convinced by the use of quadratic curves to represent strokes. Strokes can be long
and very complex. Example - a drawing of curly hair may use long, looped strokes. And strokes vary 
in width, media density and much more. I understand this is a first step - but some text that acknowledges
the very severe limitations the method operates under is, i think necessary so that the contribution can
be more fairly understood.

It’s not clear to me why the generator produces a face (in the same view angle, or its mirror, and
with the same crop window). This again is very limiting.

Results:
The authors make no experiments at all. This is a significant weakness in the paper.
Rather they show some images that have been generated, and then claim the images look good.
Unfortunately for the authors, others (like me) have a different position.
I am not convinced the drawings are “high quality” as claimed.
Especially when compared to the NPR work my view is that output produced in recent years is low quality.
And no work I have seen in comparable in quality to human art.

The fact drawing are usually made of some actual thing, like a face or a dog.
The paper never mentions how to control the output to direct it to a particular noun class.
(Does the noun class impact the embedding into latent space? I guess so - it depends on S)
All the images are of faces, and all in “manga” style.
This means the paper is not clear on its generality.
Do you have examples of other noun classes?

Conclusion:
I found the conclusion rather limited. I certainly disagree with the claim that 
  “the primary limitation lies in the probabilistic nature of the reconstruction process”.
In fact the primary limitation is much more likely to be that the system makes no use of
semantic information, other than possibly implicitly via training. It is this issue, rather than any
other, that has constrained progress in this area.

Summary:
I enjoyed the paper, in part because of the controversial claims it makes, but mostly because it
takes on a difficult problem in an imaginative way. That said, I feel the authors would do themselves and
the field much great justice if they were to resist their claims. I strongly recommend looking at some
real drawings, ideally “in the flesh” - and not just manga images of 3/4 faces, heavily cropped, drawn
with short quadratic curves of uniform width and density, on a perfectly flat surface.

The paper lacks any experiment, which was once common but is far less so now. One obvious
experiment is to conduct some kind of Turing test, of which there are many variants in the NPR/NST
literature (especially the more recent). As it stands the paper lack rigour - a rigour which I suspect would
lead the authors to question some of their more controversial (for me) claims.

The paper makes a contribution and is publishable.

### Weaknesses
 Introduction:
The introduction still makes claims about vector representations being inherently linked to creativity and pixel representations to perception, albeit in a slightly modified form. While the authors have removed some of the more subjective language, the core argument remains unsubstantiated and lacks any grounding in perceptual or art-historical literature. The assertion that vector formats allow for modeling 'additional information' beyond raster formats, specifically regarding individual strokes, is not novel and has been explored in prior work. The claim that this enables more fine-grained editing is also not unique to this method.

Related Works:
The paper still fails to cite any work prior to 2015, despite a substantial body of relevant literature in non-photorealistic rendering and vector graphics. This omission significantly undermines the paper's positioning within the field and suggests a lack of awareness of foundational work.

Method
The use of quadratic curves to represent strokes remains a significant limitation. While the authors acknowledge that strokes can be complex, the paper does not adequately address the implications of using such a simplified representation. The argument that the method is theoretically not restricted to quadratic curves is insufficient; the practical implementation and evaluation are limited to this specific case. The lack of exploration of alternative stroke representations, such as splines or more complex parametric curves, is a major weakness. The fact that the generator produces faces with consistent view angles and crops is a significant limitation, restricting the generalizability of the approach.

Results:
The lack of any quantitative experiments remains a major flaw. The claim that the generated images are 'high quality' is subjective and not supported by any objective evaluation. The comparison to existing NPR work is still unfavorable, and the absence of a Turing test or similar evaluation further weakens the paper's claims. The fact that all images are of faces, and in a specific style, makes it impossible to assess the generality of the method. The paper does not address how to control the output to generate different noun classes, and the implicit dependence on the training data for style and content is not sufficiently discussed.

Conclusion:
The conclusion still focuses on the probabilistic nature of the reconstruction process as the primary limitation, which is not the case. The lack of semantic understanding and control over the generated content is a far more significant limitation. The system's inability to generate diverse outputs, beyond faces in a specific style, is a major weakness that is not adequately addressed.

### Questions
How well do you you expect the system to generalise to?
* other objects
* other points of view
* other styles
* the true complexity of real strokes

What citable evidence do you have that vectors relate to creativity and pixels to perception?

Why did you conduct no experiment?

Why have you not cited any paper prior to 2015, when there is plenty of relevant work?

What is your defence fot the claim that "the primary limitation lies in the probabilistic nature of the reconstruction process"?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
