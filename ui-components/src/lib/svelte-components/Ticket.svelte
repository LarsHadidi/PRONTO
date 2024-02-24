<script lang="ts">
  import { page } from "$app/stores";
  export let name: string;
  export let eventName = $page.data?.[name]?.name;
  export let eventDate = $page.data?.[name]?.date;
  export let eventVenue = $page.data?.[name]?.venue;
  export let ticketId = $page.data?.[name]?.ticketid;
  const eventMonth = eventDate?.toLocaleString("default", { month: "long" });
  const eventDay = eventDate?.getDate();
</script>

<div class="ticket">
  <div class="stub">
    <div class="top">
      <span class="admit">GEBUCHT</span>
      <span class="line"></span>
      <span class="num">
        Ticket
        <span>#{ticketId}</span>
      </span>
    </div>
    <div class="invite">
      {eventMonth}<br />{eventDay}
    </div>
  </div>
  <div class="check">
    <div class="big">
      {eventName}
    </div>
    <div class="info">
      <section>
        <div class="title">Datum</div>
        <div>{eventDate.toLocaleDateString()}</div>
      </section>
      <section>
        <div class="title">Ort</div>
        <div>{eventVenue}</div>
      </section>
    </div>
  </div>
</div>

<style>
  .ticket {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 700px;
    margin: 20px auto;
    border: 1px dashed;
  }
  .ticket .stub,
  .ticket .check {
    box-sizing: border-box;
  }
  .stub {
    background: #ef5658;
    height: 250px;
    width: 250px;
    color: white;
    padding: 20px;
    position: relative;
    border-right: 1px dotted black;
  }
  .stub:before {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    border-top: 20px solid gray;
    border-left: 20px solid #ef5658;
    width: 0;
  }
  .stub:after {
    content: "";
    position: absolute;
    bottom: 0;
    right: 0;
    border-bottom: 20px solid gray;
    border-left: 20px solid #ef5658;
    width: 0;
  }
  .stub .top {
    display: flex;
    align-items: center;
    height: 40px;
    text-transform: uppercase;
  }
  .stub .top .line {
    display: block;
    background: #fff;
    height: 40px;
    width: 3px;
    margin: 0 20px;
  }
  .stub .top .num {
    font-size: 10px;
  }
  .stub .top .num span {
    color: #000;
  }
  .stub .invite {
    position: absolute;
    left: 150px;
    bottom: 45px;
    color: #000;
    width: 20%;
  }
  .stub .invite:before {
    content: "";
    background: #fff;
    display: block;
    width: 40px;
    height: 3px;
    margin-bottom: 5px;
  }
  .check {
    background: #fff;
    height: 250px;
    width: 450px;
    padding: 40px;
    position: relative;
  }
  .check:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    border-top: 20px solid gray;
    border-right: 20px solid #fff;
    width: 0;
  }
  .check:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    border-bottom: 20px solid gray;
    border-right: 20px solid #fff;
    width: 0;
  }
  .check .big {
    font-size: 80px;
    font-weight: 900;
    line-height: 0.8em;
  }
  .check .info {
    display: flex;
    justify-content: flex-start;
    font-size: 12px;
    margin-top: 20px;
    width: 100%;
  }
  .check .info section {
    margin-right: 50px;
  }
  .check .info section:before {
    content: "";
    background: #ef5658;
    display: block;
    width: 40px;
    height: 3px;
    margin-bottom: 5px;
  }
  .check .info section .title {
    font-size: 10px;
    text-transform: uppercase;
  }
</style>
