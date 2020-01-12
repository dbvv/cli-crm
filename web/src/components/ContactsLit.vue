<template>
  <div class="contact-list">
    <v-row justify="center">
      <v-dialog v-model="dialog" persistent max-width="290">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>
        </template>
        <v-card>
          <v-card-title class="headline">Use Google's location service?</v-card-title>
          <v-card-text>Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="dialog = false">Disagree</v-btn>
            <v-btn color="green darken-1" text @click="dialog = false">Agree</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <v-simple-table>
      <template v-slot:default>
        <thead>
          <th class="text-left">Name</th>
          <th class="text-left">Last Name</th>
          <th class="text-left">Phone</th>
          <th>Edit</th>
        </thead>
        <tbody>
          <tr v-for="contact in contacts" :key="contact.id">
            <td>{{contact.name}}</td>
            <td>{{contact.last_name}}</td>
            <td>{{contact.phone}}</td>
            <td></td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>

</template>


<script>
    import axios from 'axios'
    export default {
        name: 'ContactsList',
        data: () => {
          return {
            contacts: [],
            dialog: false,
          }
        },
      mounted() {
        axios.get('/api/contacts/all')
          .then(data => {
            this.contacts = data.data;
          })
      }
    }
</script>
