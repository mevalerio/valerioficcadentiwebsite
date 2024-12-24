---
title: "Kendall correlations and Radar charts in soccer rankings"
author: ["Roy Cerqueti", "Raffaele Mattera", "**Valerio Ficcadenti**"]
institute: ["Department of Social and Economic Sciences, Sapienza University of Rome, Italy", "GRANEM, University of Angers, France", "School of Business, London South Bank University, United Kingdom"]
date: "July 17, 2024"
output:
  revealjs::revealjs_presentation:
    theme: night
    highlight: zenburn
---

# Title Slide

### Kendall correlations and radar charts in soccer rankings

#### Roy Cerqueti, Raffaele Mattera, **Valerio Ficcadenti**

---

# Introduction

- Record of mathematical victory: **5 rounds in advance**
  - Torino (1946-1947), Fiorentina (1955-1956), Inter (2006-2007 and 2023-2024), Juventus (2018-2019), Napoli (2022-2023).

#### Sample Table of 2023–24 Inter Milan Season:

| Round  | 1 | 2 | 3 | 4 | ... | 36 | 37 | 38 |
|--------|---|---|---|---|-----|----|----|----|
| Result | W | W | W | W | ... | W  | D  | D  |

---

# Some Literature

- **Ausloos (2024):** New ranking indicators for cyclists based on rank-size laws.
- **Ficcadenti et al. (2023):** Football rankings as unified frameworks through rank-size analysis.
- **Sziklai et al. (2022):** Overview of tournament efficacy using Kendall correlation.
- **Cerqueti et al. (2022):** Ranking teams based on goals.
- **Ausloos et al. (2014):** Structural analysis of FIFA/UEFA rankings.

---

# Objectives and Aims

- Propose a **novel scoring rule** integrating goals scored and conceded.
- Evaluate the sensitivity of rankings to **performance-oriented metrics**.

---

# Methodology

### Four-Step Procedure:

1. Generate **unofficial rankings** ($GF_r$, $GA_r$).
2. Compute **Kendall $\tau$** correlations for all ranking pairs.
3. Create **radar charts** and normalize areas.
4. Detect rankings with a target Kendall $\tau$ correlation.

---

# Kendall $\tau$ Correlation Analysis

#### Equation:

\[
\tau_b = \frac{P - Q}{\sqrt{(P+Q+T)(P+Q+U)}}
\]

Where:
- $P$, $Q$: Concordant and discordant pairs.
- $T$, $U$: Number of ties.

---

# Mapping Correlations into Radar Charts

- Normalization formula:
  \[\tau_{b;N} = \frac{\tau_b + 1}{2}\]

- Area calculation:
  \[A = \frac{1}{2} \left| x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \right|\]

---

# Results and Discussion

### Results Overview:
- Radar chart areas transformed into target $\tau_b$ values.
- Improved performance-oriented rankings derived.

#### Example Distribution:
![Example Distribution](example_distribution.png)

---

# Conclusion & Limitations

### Conclusions:

- Proposed **new ranking framework** integrating geometric analysis and Kendall $\tau$.
- Improved reflection of offensive and defensive team capabilities.

### Limitations:

- Computational complexity.
- Sensitivity to additional metrics.

---

# Future Research

- Expand methodology to other leagues and sports.
- Incorporate additional performance metrics.
- Enhance ranking methodologies using geometric and statistical techniques.

---

# Questions?

Feel free to ask! Feedback and comments are welcome.
