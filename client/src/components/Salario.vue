<template>
    <div class="row">
        <div class="col-2"></div>
        <div v-if = "finished === false" class="col-8 text-center">
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
                      @click="verify"
                      >Calcular
                    </button>
                  </div>
                </div>
            </div>
        </div>
        <div v-else class="col-8">
            <h1 class="text-center">Resultado</h1>
            <div class="mt-5">
            <div class="row">
                <div class="col-6">
                  <h2>Salario bruto:</h2>
                  <h2>INSS:</h2>
                  <h2>Sindicato:</h2>
                  <h2>Imposto de Renda:</h2>
                  <h2 class="mt-4">Salario líquido:</h2>
                </div>
                <div class="col-6">
                  <h2 class="text-primary">+R$ {{this.salarioTotal}}</h2>
                  <h2 class="text-danger">- R$ {{this.inss}}</h2>
                  <h2 class="text-danger">- R$ {{this.sind}}</h2>
                  <h2 class="text-danger">- R$ {{this.ir}}</h2>
                  <h2 class="text-success mt-4">=R$ {{this.salarioliquido}}</h2>
                </div>
            </div>
              <div class="container mt-5">
                <div class="row">
                  <div class="col text-center">
                    <button
                      class="btn btn-primary btn-lg"
                      @click="reset">REINICIAR
                    </button>
                  </div>
                </div>
              </div>
            </div>
         </div>
        <div class="col-2">
        </div>
    </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      horastrab: '',
      valor: '',
      salarioTotal: 0,
      inss: 0,
      sind: 0,
      ir: 0,
      salarioliquido: 0,
      finished: false,
    };
  },

  methods: {

    verify() {
      if ((this.horastrab === null || this.horastrab === '') || (this.valor === null || this.valor === '')) {
        window.alert('Há campos em branco!');
      } else if (this.horastrab < 1 || this.valor < 1) {
        window.alert('Só são aceitos valores positivos!');
      } else {
        console.log(this.horastrab, this.valor);
        this.postResult();
      }
    },

    postResult() {
      this.horastrab = parseInt(this.horastrab, 10);
      this.valor = parseInt(this.valor, 10);
      const path = 'http://localhost:5000/salary';
      const payload = {
        cash: this.valor,
        jobtime: this.horastrab,
      };
      axios.post(path, payload)
        .then((res) => {
          this.salarioTotal = res.data.fullsalary;
          this.inss = res.data.inss;
          this.sind = res.data.sind;
          this.ir = res.data.ir;
          this.salarioliquido = res.data.finalsalary;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      this.finished = true;
    },
    reset() {
      this.finished = false;
      this.horastrab = null;
      this.valor = null;
    },
  },
  created() {
  },
};
</script>
