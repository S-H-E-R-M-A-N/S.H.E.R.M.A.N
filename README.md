# S.H.E.R.M.A.N.
> **S**atellite **H**igh **E**levation and **R**adar **M**onitoring **A**rrangement **N**etwork

A real-time 3D satellite tracking and orbit visualization web application built with **CesiumJS** and **Satellite.js**. S.H.E.R.M.A.N. parses Two-Line Element (TLE) set data to render accurate orbital trajectories, position vectors, and elevation profiles on an interactive globe.

---

## Overview

S.H.E.R.M.A.N. bridges orbital mechanics and web graphics by processing TLE data directly in the browser. It translates NORAD catalog entries into dynamic 3D entities over Earth's surface, allowing users to inspect individual satellite paths, ground tracks, and altitude distributions.

---

## Key Features

* **Interactive 3D Globe:** High-performance geospatial visualization powered by the CesiumJS engine.
* **SGP4 Orbital Propagation:** Uses `satellite.js` to calculate accurate real-time position and velocity from standard TLE sets.
* **Custom Entity Rendering:** Dynamic rendering of satellite markers, trajectory polyline vectors, and orbital cones.
* **Catalog Data Integration:** Compatible with TLE data streams from Space-Track and Celestrak.

---

## Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Visualization Engine:** [CesiumJS](https://cesium.com/platform/cesiumjs/)
* **Orbit Mathematics:** [Satellite.js](https://github.com/shashwatak/satellite.js)
* **Data Sources:** [Space-Track](https://www.space-track.org/)

---

## Getting Started

### Prerequisites

* A modern web browser with WebGL enabled.
* A local HTTP server (such as Live Server, Python `http.server`, or `npx http-server`).
* *(Optional)* A [Cesium ion](https://ion.cesium.com/) access token for custom terrain and imagery layers.

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/sherman.git](https://github.com/your-username/sherman.git)
   cd sherman
