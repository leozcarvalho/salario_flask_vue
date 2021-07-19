<template>
    <div class="row">
        <div class="col-2"></div>
        <div class="col-8 text-center">
            <h1 class="mb-5">Calcule o seu salário líquido
            </h1>
            <div class="mt-5">
                    <div class="row">
                    <div class="col-6 text-left">
                        <label for="inputNumber"
                        class="font-weight-bold">
                            <h2>Horas trabalhadas no mês: </h2>
                        </label>
                    </div>
                    <div class="col-4">
                        <input class = "form-control form-control-lg"
                        placeholder = "Horas trabalhadas"
                        v-model="horastrab">
                    </div>
                    <div class="col-2">
                    </div>
                    </div>
            </div>
            <div class="my-5">
                    <div class="row">
                    <div class="col-6 text-left">
                        <label for="inputNumber"
                        class="font-weight-bold">
                            <h2>Valor recebido por hora: </h2>
                        </label>
                    </div>
                    <div class="col-4">
                        <input class = "form-control form-control-lg"
                        placeholder = "Valor hora"
                        v-model="valor">
                    </div>
                    <div class="col-2">
                    </div>
                    </div>
            </div>
            <div class="container mt-5">
                <div class="row">
                  <div class="col text-center">
                    <button
                      class="btn btn-primary btn-lg"
                      @click="postResult"
                      >Calcular
                    </button>
                  </div>
                </div>
            </div>
        </div>
        <div class="col-2">
        </div>
    </div>
</template>

<script>

// import axios from 'axios';

export default {
  data() {
    return {
      horastrab: null,
      valor: null,
    };
  },

  methods: {
    postResult() {
      this.horastrab = parseInt(this.horastrab, 10);
      this.valor = parseInt(this.valor, 10);
      console.log(this.horastrab, this.valor);
    },
  },
  created() {
  },
};
</script>
