<script lang="ts">
  import {
    Heading,
    P,
    Button,
    Select,
    Input,
    Label,
    Spinner,
  } from "flowbite-svelte";
  import { onMount } from "svelte";
  import axios from "axios";
  let area = 50;
  let floor = 3;
  let has_heating = true;
  let animals_allowed = false;
  let rennovation = "Новый ремонт";
  let house_type = "Новостройка";
  let prepayment = "2 месяца";
  let district = "шохмансур";
  let bathroom = "Раздельный";
  let price: number | null = null;
  let loading = false;

  async function submitForm() {
    loading = true;
    price = null;
    const response = await axios.post("http://127.0.0.1:8000/", {
      area,
      floor,
      has_heating,
      animals_allowed,
      rennovation,
      house_type,
      prepayment,
      district,
      bathroom,
    });
    price = response.data.price;
    loading = false;
  }
</script>

<div class="text-center page">
  <Heading
    tag="h1"
    class="mb-4"
    customSize="text-4xl font-extrabold md:text-5xl lg:text-6xl"
  >
    Проверь стоимость аренды
  </Heading>
  <P class="mb-6 text-lg lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">
    Здесь вы сможете проверить рыночную стоимость аренды квартиры в городе
    Душанбе (скоро Худжанд)
  </P>
  <form on:submit|preventDefault={submitForm}>
    <div class="grid gap-6 mb-6 md:grid-cols-2">
      <div>
        <Label>Квадратура (м²)</Label><Input
          type="number"
          bind:value={area}
          min="1"
          max="200"
          required
        />
      </div>
      <div>
        <Label>Этаж</Label><Input
          type="number"
          bind:value={floor}
          min="1"
          max="23"
          required
        />
      </div>
      <div>
        <Label>Отопление</Label><Select bind:value={has_heating}
          ><option value={true}>Есть</option><option value={false}>Нет</option
          ></Select
        >
      </div>
      <div>
        <Label>Домашние животные</Label><Select bind:value={animals_allowed}
          ><option value={true}>Разрешены</option><option value={false}
            >Запрещены</option
          ></Select
        >
      </div>
      <div>
        <Label>Ремонт</Label><Select bind:value={rennovation}
          ><option>Новый ремонт</option><option>С ремонтом</option><option
            >Без ремонта (коробка)</option
          ></Select
        >
      </div>
      <div>
        <Label>Тип дома</Label><Select bind:value={house_type}
          ><option>Новостройка</option><option>Советский дом</option></Select
        >
      </div>
      <div>
        <Label>Предоплата</Label><Select bind:value={prepayment}
          ><option>2 месяца</option><option>3 месяца</option><option
            >6 месяцев</option
          ><option>12 месяцев</option><option>Без предоплаты</option></Select
        >
      </div>
      <div>
        <Label>Район</Label><Select bind:value={district}
          ><option value="шохмансур">Шохмансур</option><option value="домпечать"
            >Дом печать</option
          ><option value="другие">Другой район</option><option value="караболо"
            >Караболо</option
          ><option value="сино">Сино</option><option value="садбарг"
            >Садбарг</option
          ><option value="102мкр">102 мкр.</option><option value="исомони"
            >Исмоили Сомони</option
          ><option value="ашан">Ашан</option><option value="овир">Овир</option
          ><option value="91мкр">91 мкр.</option><option value="спартак"
            >Спартак</option
          ><option value="зарафшон">Зарафшон</option><option value="фирдавси"
            >Фирдавси</option
          ><option value="профсоюз">Профсоюз</option><option value="92мкр"
            >92 мкр.</option
          ><option value="цум">ЦУМ</option><option value="алфемо"
            >Альфемо</option
          ><option value="ватан">Ватан</option><option value="112мкр"
            >112 мкр.</option
          ><option value="82мкр">82 мкр.</option><option value="мехргон"
            >Мехргон</option
          ><option value="84мкр">84 мкр.</option><option value="воданасос"
            >Водонасос</option
          ></Select
        >
      </div>
      <div>
        <Label>Санузел</Label><Select bind:value={bathroom}
          ><option>Раздельный</option><option>Совмещенный</option></Select
        >
      </div>
    </div>
    <Button type="submit" class="w-full">Рассчитать стоимость</Button>
  </form>
  {#if loading}<div class="mt-4"><Spinner size="lg" /> Загружаем...</div>{/if}
  {#if price !== null}
    <div class="mt-6 text-2xl font-bold">
      Оценочная стоимость: {price} сомони
    </div>
  {/if}
</div>

<style>
  .page {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }
</style>
