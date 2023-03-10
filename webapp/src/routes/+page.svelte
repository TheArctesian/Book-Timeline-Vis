<script>
  import data from "../Data/merged_file.json";
  import "../app.css";
  console.log(data);
  data.sort(function (a, b) {
    return a.year - b.year;
  });

  let showBooks = 1;
  let showMovies = 1;
  function toggleBook() {
    if (showBooks == 1) {
      showBooks = 0;
    } else {
      showBooks = 1;
    }
  }
  function toggleMovie() {
    if (showMovies == 1) {
      showMovies = 0;
    } else {
      showMovies = 1;
    }
    console.log(showMovies);
  }
</script>

<h1>Media Timeline</h1>
<div class="container">
  {#each data as i}
    {#if i.views != 0}
      {#if i.type == "Book" && showBooks == 1}
        <div class="media book">
          <h1>{i.type}</h1>
          <p>{i.title} <b class="bold">- {i.author}</b></p>
          <h1 class="yearB">{i.year}</h1>
        </div>
      {/if}
      {#if i.type == "Movie" && showMovies == 1}
        <div class="media Movie">
          <h1>{i.type}</h1>
          <p>{i.title} <b class="bold">{i.author}</b></p>
          <h1 class="yearM">{i.year}</h1>
        </div>
      {/if}
    {/if}
  {/each}
</div>
<div class="buttons">
  {#if showBooks == 1}
    <button on:click={toggleBook}>Toggle Books</button>
  {/if}
  {#if showBooks == 0}
    <button class="buttonOff" on:click={toggleBook}>Toggle Books</button>
  {/if}
  {#if showMovies == 1}
    <button on:click={toggleMovie}>Toggle Movies</button>
  {/if}
  {#if showMovies == 0}
    <button class="buttonOff" on:click={toggleMovie}>Toggle Movies</button>
  {/if}
</div>

<style>
  h1 {
    text-align: center;
    color: var(--fg);
  }
  p {
    width: 30vw;
    height: 20vh;
    text-align: center;
  }
  .Movie {
    border: 5px dotted var(--yellow);
  }
  .book {
    box-shadow: 12px 5px #323641;
    border: 5px solid var(--purple);
  }
  .media {
    display: flex;
    flex-flow: column nowrap;
    background-color: var(--selection);
    width: fit-content;
    padding: 1rem;
    margin: 2rem;
    margin-top: auto;
    color: var(--white);
    border-radius: 0.2rem;
  }
  .container {
    padding: 1rem;
    margin: 1rem;
    display: flex;
    height: fit-content;
    overflow: scroll;
    scroll-behavior: smooth;
    overflow-y: hidden; /* Hide vertical scrollbar */
  }
  /* width */
  ::-webkit-scrollbar {
    width: 10px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: var(--selection);
    border-radius: 1rem;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    border-radius: 1rem;
    background: var(--purple);
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: var(--cyan);
  }

  .yearB {
    margin-top: auto;
    color: var(--purple);
  }
  .yearM {
    margin-top: auto;
    color: var(--yellow);
  }
  .buttons{
    display: flex;
  }
  button {
    margin: auto;
    background-color: var(--purple);
    border: none;
    color: var(--white);
    padding: 1rem;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 0.2rem;
  }
  .buttonOff {
    transition: all ease-in-out 500ms;
    background-color: var(--selection);
  }
</style>
